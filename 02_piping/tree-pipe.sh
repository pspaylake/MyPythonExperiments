#!/bin/bash

echo "Example of piping with the tree command (first 5 lines):"
tree ~ | head -n 5

echo "Example of piping with the tree command (last 5 lines):"
tree ~ | tail -n 5