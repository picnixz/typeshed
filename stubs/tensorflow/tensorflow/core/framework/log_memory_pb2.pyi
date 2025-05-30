"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import typing

import google.protobuf.descriptor
import google.protobuf.message
import tensorflow.core.framework.tensor_description_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class MemoryLogStep(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STEP_ID_FIELD_NUMBER: builtins.int
    HANDLE_FIELD_NUMBER: builtins.int
    step_id: builtins.int
    """Process-unique step id."""
    handle: builtins.str
    """Handle describing the feeds and fetches of the step."""
    def __init__(self, *, step_id: builtins.int | None = ..., handle: builtins.str | None = ...) -> None: ...
    def ClearField(self, field_name: typing.Literal["handle", b"handle", "step_id", b"step_id"]) -> None: ...

global___MemoryLogStep = MemoryLogStep

@typing.final
class MemoryLogTensorAllocation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STEP_ID_FIELD_NUMBER: builtins.int
    KERNEL_NAME_FIELD_NUMBER: builtins.int
    TENSOR_FIELD_NUMBER: builtins.int
    step_id: builtins.int
    """Process-unique step id."""
    kernel_name: builtins.str
    """Name of the kernel making the allocation as set in GraphDef,
    e.g., "affine2/weights/Assign".
    """
    @property
    def tensor(self) -> tensorflow.core.framework.tensor_description_pb2.TensorDescription:
        """Allocated tensor details."""

    def __init__(
        self,
        *,
        step_id: builtins.int | None = ...,
        kernel_name: builtins.str | None = ...,
        tensor: tensorflow.core.framework.tensor_description_pb2.TensorDescription | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["tensor", b"tensor"]) -> builtins.bool: ...
    def ClearField(
        self, field_name: typing.Literal["kernel_name", b"kernel_name", "step_id", b"step_id", "tensor", b"tensor"]
    ) -> None: ...

global___MemoryLogTensorAllocation = MemoryLogTensorAllocation

@typing.final
class MemoryLogTensorDeallocation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ALLOCATION_ID_FIELD_NUMBER: builtins.int
    ALLOCATOR_NAME_FIELD_NUMBER: builtins.int
    allocation_id: builtins.int
    """Id of the tensor buffer being deallocated, used to match to a
    corresponding allocation.
    """
    allocator_name: builtins.str
    """Name of the allocator used."""
    def __init__(self, *, allocation_id: builtins.int | None = ..., allocator_name: builtins.str | None = ...) -> None: ...
    def ClearField(
        self, field_name: typing.Literal["allocation_id", b"allocation_id", "allocator_name", b"allocator_name"]
    ) -> None: ...

global___MemoryLogTensorDeallocation = MemoryLogTensorDeallocation

@typing.final
class MemoryLogTensorOutput(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STEP_ID_FIELD_NUMBER: builtins.int
    KERNEL_NAME_FIELD_NUMBER: builtins.int
    INDEX_FIELD_NUMBER: builtins.int
    TENSOR_FIELD_NUMBER: builtins.int
    step_id: builtins.int
    """Process-unique step id."""
    kernel_name: builtins.str
    """Name of the kernel producing an output as set in GraphDef, e.g.,
    "affine2/weights/Assign".
    """
    index: builtins.int
    """Index of the output being set."""
    @property
    def tensor(self) -> tensorflow.core.framework.tensor_description_pb2.TensorDescription:
        """Output tensor details."""

    def __init__(
        self,
        *,
        step_id: builtins.int | None = ...,
        kernel_name: builtins.str | None = ...,
        index: builtins.int | None = ...,
        tensor: tensorflow.core.framework.tensor_description_pb2.TensorDescription | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["tensor", b"tensor"]) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing.Literal["index", b"index", "kernel_name", b"kernel_name", "step_id", b"step_id", "tensor", b"tensor"],
    ) -> None: ...

global___MemoryLogTensorOutput = MemoryLogTensorOutput

@typing.final
class MemoryLogRawAllocation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STEP_ID_FIELD_NUMBER: builtins.int
    OPERATION_FIELD_NUMBER: builtins.int
    NUM_BYTES_FIELD_NUMBER: builtins.int
    PTR_FIELD_NUMBER: builtins.int
    ALLOCATION_ID_FIELD_NUMBER: builtins.int
    ALLOCATOR_NAME_FIELD_NUMBER: builtins.int
    step_id: builtins.int
    """Process-unique step id."""
    operation: builtins.str
    """Name of the operation making the allocation."""
    num_bytes: builtins.int
    """Number of bytes in the allocation."""
    ptr: builtins.int
    """Address of the allocation."""
    allocation_id: builtins.int
    """Id of the tensor buffer being allocated, used to match to a
    corresponding deallocation.
    """
    allocator_name: builtins.str
    """Name of the allocator used."""
    def __init__(
        self,
        *,
        step_id: builtins.int | None = ...,
        operation: builtins.str | None = ...,
        num_bytes: builtins.int | None = ...,
        ptr: builtins.int | None = ...,
        allocation_id: builtins.int | None = ...,
        allocator_name: builtins.str | None = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "allocation_id",
            b"allocation_id",
            "allocator_name",
            b"allocator_name",
            "num_bytes",
            b"num_bytes",
            "operation",
            b"operation",
            "ptr",
            b"ptr",
            "step_id",
            b"step_id",
        ],
    ) -> None: ...

global___MemoryLogRawAllocation = MemoryLogRawAllocation

@typing.final
class MemoryLogRawDeallocation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STEP_ID_FIELD_NUMBER: builtins.int
    OPERATION_FIELD_NUMBER: builtins.int
    ALLOCATION_ID_FIELD_NUMBER: builtins.int
    ALLOCATOR_NAME_FIELD_NUMBER: builtins.int
    DEFERRED_FIELD_NUMBER: builtins.int
    step_id: builtins.int
    """Process-unique step id."""
    operation: builtins.str
    """Name of the operation making the deallocation."""
    allocation_id: builtins.int
    """Id of the tensor buffer being deallocated, used to match to a
    corresponding allocation.
    """
    allocator_name: builtins.str
    """Name of the allocator used."""
    deferred: builtins.bool
    """True if the deallocation is queued and will be performed later,
    e.g. for GPU lazy freeing of buffers.
    """
    def __init__(
        self,
        *,
        step_id: builtins.int | None = ...,
        operation: builtins.str | None = ...,
        allocation_id: builtins.int | None = ...,
        allocator_name: builtins.str | None = ...,
        deferred: builtins.bool | None = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing.Literal[
            "allocation_id",
            b"allocation_id",
            "allocator_name",
            b"allocator_name",
            "deferred",
            b"deferred",
            "operation",
            b"operation",
            "step_id",
            b"step_id",
        ],
    ) -> None: ...

global___MemoryLogRawDeallocation = MemoryLogRawDeallocation
