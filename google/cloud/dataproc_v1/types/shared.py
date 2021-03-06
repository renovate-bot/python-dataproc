# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import proto  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.dataproc.v1", manifest={"Component",},
)


class Component(proto.Enum):
    r"""Cluster components that can be activated.
    Next ID: 16.
    """
    COMPONENT_UNSPECIFIED = 0
    ANACONDA = 5
    DOCKER = 13
    DRUID = 9
    FLINK = 14
    HBASE = 11
    HIVE_WEBHCAT = 3
    JUPYTER = 1
    PRESTO = 6
    RANGER = 12
    SOLR = 10
    ZEPPELIN = 4
    ZOOKEEPER = 8


__all__ = tuple(sorted(__protobuf__.manifest))
