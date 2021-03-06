# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import helloworld_pb2 as helloworld__pb2


class GreeterStub(object):
  """The greeting service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Add = channel.unary_unary(
        '/helloworld.Greeter/Add',
        request_serializer=helloworld__pb2.AddRequest.SerializeToString,
        response_deserializer=helloworld__pb2.AddReply.FromString,
        )


class GreeterServicer(object):
  """The greeting service definition.
  """

  def Add(self, request, context):
    """Sends a greeting
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Add': grpc.unary_unary_rpc_method_handler(
          servicer.Add,
          request_deserializer=helloworld__pb2.AddRequest.FromString,
          response_serializer=helloworld__pb2.AddReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'helloworld.Greeter', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
