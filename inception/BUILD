# Description:
# TensorFlow models for Places205.

package(default_visibility = [":internal"])

licenses(["notice"])  # Apache 2.0

exports_files(["LICENSE"])

package_group(
    name = "internal",
    packages = ["//inception/..."],
)

py_library(
    name = "dataset",
    srcs = [
        "dataset.py",
    ],
)

py_library(
    name = "place_data",
    srcs = [
        "place_data.py",
    ],
    deps = [
        ":dataset",
    ],
)

py_library(
    name = "image_processing",
    srcs = [
        "image_processing.py",
    ],
)

py_library(
    name = "inception",
    srcs = [
        "inception_model.py",
    ],
    visibility = ["//visibility:public"],
    deps = [
        ":dataset",
        "//inception/slim",
    ],
)

py_binary(
    name = "place_eval",
    srcs = [
        "place_eval.py",
    ],
    deps = [
        ":place_data",
        ":inception_eval",
    ],
)

py_library(
    name = "inception_eval",
    srcs = [
        "inception_eval.py",
    ],
    deps = [
        ":image_processing",
        ":inception",
    ],
)

py_binary(
    name = "place_train",
    srcs = [
        "place_train.py",
    ],
    deps = [
        ":place_data",
        ":inception_train",
    ],
)


py_library(
    name = "inception_train",
    srcs = [
        "inception_train.py",
    ],
    deps = [
        ":image_processing",
        ":inception",
    ],
)

py_binary(
    name = "build_image_data",
    srcs = ["data/build_image_data.py"],
)

filegroup(
    name = "srcs",
    srcs = glob(
        [
            "**/*.py",
            "BUILD",
        ],
    ),
)

