OPENQASM 2.0;

include "qelib1.inc";

gate rcccx_dg a,b,c,d {
    u2(-2*pi,pi) d;
    u1(pi/4) d;
    cx c,d;
    u1(-pi/4) d;
    u2(-2*pi,pi) d;
    u1(pi/4) d;
    cx b,d;
    u1(-pi/4) d;
    cx a,d;
    u1(pi/4) d;
    cx b,d;
    u1(-pi/4) d;
    cx a,d;
    u2(-2*pi,pi) d;
    u1(pi/4) d;
    cx c,d;
    u1(-pi/4) d;
    u2(-2*pi,pi) d;
}

gate rcccx a,b,c,d { u2(0,pi) d;
    u1(pi/4) d;
    cx c,d;
    u1(-pi/4) d;
    u2(0,pi) d;
    cx a,d;
    u1(pi/4) d;
    cx b,d;
    u1(-pi/4) d;
    cx a,d;
    u1(pi/4) d;
    cx b,d;
    u1(-pi/4) d;
    u2(0,pi) d;
    u1(pi/4) d;
    cx c,d;
    u1(-pi/4) d;
    u2(0,pi) d;
 }

gate mcx a,b,c,d,e {
    h e;
 cu1(pi/2) d,e;
 h e;
 rcccx a,b,c,d;
 h e;
 cu1(-pi/2) d,e;
 h e;
 rcccx_dg a,b,c,d;
 c3sx a,b,c,e;
 }
qreg qr[5];

creg cr[5];

mcx qr[0],qr[1],qr[2],qr[3],qr[4];
