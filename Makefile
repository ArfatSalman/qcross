SHELL := /bin/bash

start:
	python3 -m qcross.start

start-new:
	python3 -m qcross.start --run-new-programs

clean:
	python3 clean.py

summary:
	python3 -m qcross.summarize qcross/summarize

run-qvm:
	qvm -S --log-level warning --compile --optimization-level 3

run-quilc:
	quilc -S --quiet --prefer-gate-ladders --log-level notice --protoquil --enable-state-prep-reductions