#!/usr/bin/env python
"""
Copyright 2022 Vadim Khitrin <me@vkhitrin.com>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


class jiavException(Exception):
    """
    Base jiav exception
    """

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class NoJiraRestAPIEndpoint(jiavException):
    """
    Raised when failed to fetch content because of permissions
    """

    def __init__(self, url, endpoint):
        message = f"Provided url '{url}' does not serve Jira Rest API at '{endpoint}'"
        super().__init__(message)


class PermissionsError(jiavException):
    """
    Raised when failed to fetch content because of permissions
    """

    def __init__(self, issue):
        message = (
            f"You do not have permissions to view {issue}, "
            "please ensure you are using the correct token."
        )
        super().__init__(message)


class IssueNotExists(jiavException):
    """
    Raised when no valid issues were found
    """

    def __init__(self, issue):
        message = f"Issue {issue} does not exist."
        super().__init__(message)


class JQLError(jiavException):
    """
    Raised when JQL error occurs
    """

    def __init__(self, jql, err):
        message = f"{err}.\nQuery is: {jql}"
        super().__init__(message)


class JQLReturnedNothing(jiavException):
    """
    Raised when JQL returns no issues
    """

    def __init__(self, jql):
        message = (
            "No issues returned by query, please ensure your query is "
            "and you are using the correct token."
            f"\nQuery is: {jql}"
        )
        super().__init__(message)


class InvalidKeyInJQL(jiavException):
    """
    Raised when an invalid key in JQL
    """

    def __init__(self, jql, err):
        message = f"{err}.\nQuery is: {jql}"
        super().__init__(message)


class JiraUnhandledException(jiavException):
    """
    Raised when an unhandled exception is raised by
    requests.exceptions.HTTPError
    """

    def __init__(self):
        message = "Unhandled excpetion was raised, please report it"
        super().__init__(message)


class InvalidYAMLException(jiavException):
    """
    Raised when an invalid YAML is supplied
    """

    def __init__(self, py_err):
        super().__init__(str(py_err))


class InvalidManifestException(jiavException):
    """
    Raised when an invalid manifest is supplied
    """

    def __init__(self, py_err):
        super().__init__(str(py_err))


class InvalidBackend(jiavException):
    """
    Raised when an unsupported backend is requested
    """

    def __init__(self, backend):
        message = "{} is not a supported backend".format(backend)
        super().__init__(message)
