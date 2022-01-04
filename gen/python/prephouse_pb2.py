# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: prephouse.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fprephouse.proto\"\x1b\n\x05Video\x12\x12\n\x04link\x18\x01 \x01(\tR\x04link\"\x9a\x03\n\x08\x46\x65\x65\x64\x62\x61\x63k\x12-\n\x08\x63\x61tegory\x18\x01 \x01(\x0e\x32\x11.Feedback.FeatureR\x08\x63\x61tegory\x12\x1d\n\x07\x63omment\x18\x02 \x01(\tH\x00R\x07\x63omment\x88\x01\x01\x12\x14\n\x05score\x18\x03 \x01(\x02R\x05score\x12#\n\nconfidence\x18\x04 \x01(\x05H\x01R\nconfidence\x88\x01\x01\x12\"\n\ntime_start\x18\x05 \x01(\x02H\x02R\ttimeStart\x88\x01\x01\x12\x1e\n\x08time_end\x18\x06 \x01(\x02H\x03R\x07timeEnd\x88\x01\x01\"\x89\x01\n\x07\x46\x65\x61ture\x12\x1d\n\x19\x46\x45\x41TURE_PAUSE_UNSPECIFIED\x10\x00\x12\x12\n\x0e\x46\x45\x41TURE_VOLUME\x10\x01\x12\x11\n\rFEATURE_LIGHT\x10\x02\x12\x10\n\x0c\x46\x45\x41TURE_GAZE\x10\x03\x12\x13\n\x0f\x46\x45\x41TURE_EMOTION\x10\x04\x12\x11\n\rFEATURE_PITCH\x10\x05\x42\n\n\x08_commentB\r\n\x0b_confidenceB\r\n\x0b_time_startB\x0b\n\t_time_end\"5\n\x0c\x46\x65\x65\x64\x62\x61\x63kList\x12%\n\x08\x66\x65\x65\x64\x62\x61\x63k\x18\x01 \x03(\x0b\x32\t.FeedbackR\x08\x66\x65\x65\x64\x62\x61\x63k29\n\x0fPrephouseEngine\x12&\n\x0bGetFeedback\x12\x06.Video\x1a\r.FeedbackList\"\x00\x42\x12\x42\x0ePrephouseProtoP\x01\x62\x06proto3')



_VIDEO = DESCRIPTOR.message_types_by_name['Video']
_FEEDBACK = DESCRIPTOR.message_types_by_name['Feedback']
_FEEDBACKLIST = DESCRIPTOR.message_types_by_name['FeedbackList']
_FEEDBACK_FEATURE = _FEEDBACK.enum_types_by_name['Feature']
Video = _reflection.GeneratedProtocolMessageType('Video', (_message.Message,), {
  'DESCRIPTOR' : _VIDEO,
  '__module__' : 'prephouse_pb2'
  # @@protoc_insertion_point(class_scope:Video)
  })
_sym_db.RegisterMessage(Video)

Feedback = _reflection.GeneratedProtocolMessageType('Feedback', (_message.Message,), {
  'DESCRIPTOR' : _FEEDBACK,
  '__module__' : 'prephouse_pb2'
  # @@protoc_insertion_point(class_scope:Feedback)
  })
_sym_db.RegisterMessage(Feedback)

FeedbackList = _reflection.GeneratedProtocolMessageType('FeedbackList', (_message.Message,), {
  'DESCRIPTOR' : _FEEDBACKLIST,
  '__module__' : 'prephouse_pb2'
  # @@protoc_insertion_point(class_scope:FeedbackList)
  })
_sym_db.RegisterMessage(FeedbackList)

_PREPHOUSEENGINE = DESCRIPTOR.services_by_name['PrephouseEngine']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'B\016PrephouseProtoP\001'
  _VIDEO._serialized_start=19
  _VIDEO._serialized_end=46
  _FEEDBACK._serialized_start=49
  _FEEDBACK._serialized_end=459
  _FEEDBACK_FEATURE._serialized_start=267
  _FEEDBACK_FEATURE._serialized_end=404
  _FEEDBACKLIST._serialized_start=461
  _FEEDBACKLIST._serialized_end=514
  _PREPHOUSEENGINE._serialized_start=516
  _PREPHOUSEENGINE._serialized_end=573
# @@protoc_insertion_point(module_scope)