#!/usr/bin/env python

import scipy.io.wavfile as wavfile
import numpy as np
from matplotlib import pyplot as plt
import sys
import os
import audioop as ao

def print_usage():
    print("Usage:")
    print("   ", sys.argv[0], " WAVFILE")
    print("Description:")
    print("   transfer the 16-bit mono WAVEFILE into A-Law(G711a, 8KHz and 8bit) format")
    print("   then transferred back to pcm files:")
    print("   WAVFILE.alaw.16.wav:  pcm-> alaw -> 16-bit-width 8KHz pcm file")
    print("   WAVFILE.alaw.8.wav:   pcm-> alaw -> 8-bit-width 8KHz pcm file")
    

def sanity_check():
    al = len(sys.argv)
    
    if al > 2 or al < 2:
        print_usage()
        exit(1)

    if not os.path.exists(sys.argv[1]):
        print(sys.argv[1], " NOT exist!")
        print_usage()
        exit(1)


def main():
    sanity_check()
    wf = sys.argv[1]
    sr, data = wavfile.read(wf)

    alaw = ao.lin2alaw(data, 2)
    out16 = ao.alaw2lin(alaw, 2)
    out8 = ao.alaw2lin(alaw, 1)
    out8 = ao.bias(out8, 1, 128)

    wavfile.write(wf+".alaw.16.wav", sr, np.frombuffer(out16, dtype=np.int16))
    wavfile.write(wf+".alaw.8.wav", sr, np.frombuffer(out8, dtype=np.int8))


if __name__ == "__main__":
    main()
