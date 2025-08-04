#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#

from transom.planocommands import *

@command
def test():
    render()
    check_links()
    check_files()

    with temp_dir() as temp:
        with working_env(HOME=temp):
            run("cat docs/install.sh | sh", shell=True)
            run("cat docs/uninstall.sh | sh", shell=True)

        generate_examples(output_dir=temp)
        generate_releases(output_dir=temp)
        generate_scripts(output_dir=temp)

@command
def update_transom():
    """
    Update the embedded Transom repo
    """
    update_external_from_github("external/transom", "ssorj", "transom")
