import prime_generator as pg
import math_functions as mf

def get_bits():
    print("Generating keys (one-time procedure).")
    while True:
        try:
            bits = int(input("Key length (bits)?\n> "))
            if bits >= 128 and mf.poweroftwocheck(bits):
                print("Key length okay...generating keys.")
                return bits
            else:
                print("ERR: Key length must be a power of two and greater than or equal to 128.")
        except (TypeError, ValueError):
            print("ERR: Enter a valid key length.")

def gen_keys(bits):
    p = pg.driver(bits//2)
    q = pg.driver(bits//2)
    n = p*q
    lambda_ = mf.lcm((p-1), (q-1))
    e = 65537
    d = mf.modinv(e, lambda_)
    d_p = d % (p-1)
    d_q = d % (q-1)
    q_inv = mf.modinv(q, p)
    return [p, q, n, e, d_p, d_q, q_inv, bits]

def enc(m, e, n):
    c = pow(m, e, n)
    return c

def dec(c, p, q, d_p, d_q, q_inv):
    m = mf.cra(c, p, q, d_p, d_q, q_inv)
    return m
