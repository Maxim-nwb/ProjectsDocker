#!/usr/bin/env python

import subprocess
import sys

subprocess.check_call([sys.executable, "-m", "pip", "install", "confluent-kafka"])