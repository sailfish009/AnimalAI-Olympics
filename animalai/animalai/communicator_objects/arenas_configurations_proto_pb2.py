# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: animalai/communicator_objects/arenas_configurations_proto.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from animalai.communicator_objects import (
    arena_configuration_proto_pb2 as animalai_dot_communicator__objects_dot_arena__configuration__proto__pb2,
)


DESCRIPTOR = _descriptor.FileDescriptor(
    name="animalai/communicator_objects/arenas_configurations_proto.proto",
    package="communicator_objects",
    syntax="proto3",
    serialized_pb=_b(
        '\n?animalai/communicator_objects/arenas_configurations_proto.proto\x12\x14\x63ommunicator_objects\x1a=animalai/communicator_objects/arena_configuration_proto.proto"\xd4\x01\n\x19\x41renasConfigurationsProto\x12K\n\x06\x61renas\x18\x01 \x03(\x0b\x32;.communicator_objects.ArenasConfigurationsProto.ArenasEntry\x12\x0c\n\x04seed\x18\x02 \x01(\x05\x1a\\\n\x0b\x41renasEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12<\n\x05value\x18\x02 \x01(\x0b\x32-.communicator_objects.ArenaConfigurationProto:\x02\x38\x01\x42\x14\xaa\x02\x11\x41\x41IOCommunicatorsb\x06proto3'
    ),
    dependencies=[
        animalai_dot_communicator__objects_dot_arena__configuration__proto__pb2.DESCRIPTOR,
    ],
)


_ARENASCONFIGURATIONSPROTO_ARENASENTRY = _descriptor.Descriptor(
    name="ArenasEntry",
    full_name="communicator_objects.ArenasConfigurationsProto.ArenasEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="communicator_objects.ArenasConfigurationsProto.ArenasEntry.key",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="communicator_objects.ArenasConfigurationsProto.ArenasEntry.value",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b("8\001")),
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=273,
    serialized_end=365,
)

_ARENASCONFIGURATIONSPROTO = _descriptor.Descriptor(
    name="ArenasConfigurationsProto",
    full_name="communicator_objects.ArenasConfigurationsProto",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="arenas",
            full_name="communicator_objects.ArenasConfigurationsProto.arenas",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="seed",
            full_name="communicator_objects.ArenasConfigurationsProto.seed",
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[_ARENASCONFIGURATIONSPROTO_ARENASENTRY,],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=153,
    serialized_end=365,
)

_ARENASCONFIGURATIONSPROTO_ARENASENTRY.fields_by_name[
    "value"
].message_type = (
    animalai_dot_communicator__objects_dot_arena__configuration__proto__pb2._ARENACONFIGURATIONPROTO
)
_ARENASCONFIGURATIONSPROTO_ARENASENTRY.containing_type = _ARENASCONFIGURATIONSPROTO
_ARENASCONFIGURATIONSPROTO.fields_by_name[
    "arenas"
].message_type = _ARENASCONFIGURATIONSPROTO_ARENASENTRY
DESCRIPTOR.message_types_by_name[
    "ArenasConfigurationsProto"
] = _ARENASCONFIGURATIONSPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ArenasConfigurationsProto = _reflection.GeneratedProtocolMessageType(
    "ArenasConfigurationsProto",
    (_message.Message,),
    dict(
        ArenasEntry=_reflection.GeneratedProtocolMessageType(
            "ArenasEntry",
            (_message.Message,),
            dict(
                DESCRIPTOR=_ARENASCONFIGURATIONSPROTO_ARENASENTRY,
                __module__="animalai.communicator_objects.arenas_configurations_proto_pb2"
                # @@protoc_insertion_point(class_scope:communicator_objects.ArenasConfigurationsProto.ArenasEntry)
            ),
        ),
        DESCRIPTOR=_ARENASCONFIGURATIONSPROTO,
        __module__="animalai.communicator_objects.arenas_configurations_proto_pb2"
        # @@protoc_insertion_point(class_scope:communicator_objects.ArenasConfigurationsProto)
    ),
)
_sym_db.RegisterMessage(ArenasConfigurationsProto)
_sym_db.RegisterMessage(ArenasConfigurationsProto.ArenasEntry)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(
    descriptor_pb2.FileOptions(), _b("\252\002\021AAIOCommunicators")
)
_ARENASCONFIGURATIONSPROTO_ARENASENTRY.has_options = True
_ARENASCONFIGURATIONSPROTO_ARENASENTRY._options = _descriptor._ParseOptions(
    descriptor_pb2.MessageOptions(), _b("8\001")
)
# @@protoc_insertion_point(module_scope)