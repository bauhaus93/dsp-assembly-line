#!/bin/sh

python dsp.py | dot -T png -o graph.png && \
	feh graph.png
