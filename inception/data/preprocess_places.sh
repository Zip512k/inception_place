#!/bin/bash

set -e

DATA_DIR="/home/qiong/Documents/DATA/places205"
SCRATCH_DIR="${DATA_DIR}/raw-data"
TRAIN_DIRECTORY="${DATA_DIR}/train"
VALIDATION_DIRECTORY="${DATA_DIR}/validation"

LABELS_FILE="${DATA_DIR}/labels.txt"
ls -1 "${SCRATCH_DIR}" | sort > "${LABELS_FILE}"

