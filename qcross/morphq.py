from os.path import join
import traceback
from functools import reduce

from termcolor import colored

from lib.qmt import (
    QiskitFuzzer,
    create_follow,
    fuzz_source_program,
    load_config_and_check,
    setup_environment,
    dump_all_metadata,
)


# Taken from MorphQ library and adapted to work with QCross
class MorphQAdaptor:
    def __init__(self, config_file_path="config/qcross.yaml"):
        self.config_file_path = config_file_path
        self.config = load_config_and_check(config_file_path)
        setup_environment(
            experiment_folder=self.config["experiment_folder"],
            folder_structure=self.config["folder_structure"],
        )
        self.generator = eval(self.config["generation_strategy"]["generator_object"])()

    def reconstruct_changed_qubit_order_result(self, result_b, full_mapping):

        full_mapping = {int(key): val for key, val in full_mapping.items()}

        def _read_str_with_mapping(bitstring: str, direct_mapping) -> str:
            """Given a bitstring convert it to the original mapping."""
            n_bits = len(bitstring)
            bitstring = bitstring[::-1]
            return "".join([bitstring[direct_mapping[i]] for i in range(n_bits)])[::-1]

        result_b = {
            _read_str_with_mapping(bitstring, full_mapping): freq
            for bitstring, freq in result_b.items()
        }

        return result_b

    def reconstruct_partitioned_results(self, results, full_mapping):
        # print("Reconstructing results")
        # print(full_mapping)

        if not isinstance(results, list):
            raise ValueError("Results should be a list")

        def _read_str_with_mapping(bitstring: str, direct_mapping) -> str:
            """Given a bitstring convert it to the original mapping."""
            n_bits = len(bitstring)
            bitstring = bitstring[::-1]
            return "".join([bitstring[direct_mapping[str(i)]] for i in range(n_bits)])[
                ::-1
            ]

        def _reconstruct(counts):
            """Pass the count results.

            NB: list the circuit working on lower qubit indices first.
            """
            result_concatenated = reduce(
                lambda counts_1, counts_2: {
                    k2 + k1: v1 * v2
                    for k1, v1 in counts_1.items()
                    for k2, v2 in counts_2.items()
                },
                counts,
            )

            result_b = {
                _read_str_with_mapping(bitstring, full_mapping): freq
                for bitstring, freq in result_concatenated.items()
            }
            return result_b

        return _reconstruct(results)

    def produce_qiskit_program_couple(self):
        experiment_folder = self.config["experiment_folder"]
        program_id, metadata_source = fuzz_source_program(
            self.generator,
            experiment_folder=experiment_folder,
            config_generation=self.config["generation_strategy"],
            config=self.config,
        )
        try:
            metadata_followup, transformation = create_follow(
                metadata_source, self.config
            )
        except Exception as error:
            print(f"Program id: {program_id}")
            print(colored(f"Could not create followup. Exception: {error}", "red"))
            if "Source = Follow" not in str(error):
                traceback.print_exc()
            return

        all_metadata = dump_all_metadata(
            out_folder=join(self.config["experiment_folder"], "programs", "metadata"),
            program_id=program_id,
            source=metadata_source,
            followup=metadata_followup,
        )

        return {
            "program_id": program_id,
            "qiskit_source_code": open(
                metadata_source["py_file_path"], "r", encoding="utf-8"
            ).read(),
            "all_metadata": all_metadata,
            "qiskit_followup_code": open(
                metadata_followup["py_file_path"], "r", encoding="utf-8"
            ).read(),
        }
