#!/usr/bin/env bash
#This file lists all individuals who contributed to this repository

set -e
cd "$(dirname"$(readlink-f"$BASH_SOURCE")")/.."

{
	cat<<-'EOH'
	EOH
	echo
	git log--format='%aN' | LC_ALL=C.UTF-8 sort -f
} > AUTHORS
