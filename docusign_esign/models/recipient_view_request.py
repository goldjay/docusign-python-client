# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class RecipientViewRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, assertion_id=None, authentication_instant=None, authentication_method=None, client_user_id=None, email=None, ping_frequency=None, ping_url=None, recipient_id=None, return_url=None, security_domain=None, user_id=None, user_name=None, x_frame_options=None, x_frame_options_allow_from_url=None):
        """
        RecipientViewRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'assertion_id': 'str',
            'authentication_instant': 'str',
            'authentication_method': 'str',
            'client_user_id': 'str',
            'email': 'str',
            'ping_frequency': 'str',
            'ping_url': 'str',
            'recipient_id': 'str',
            'return_url': 'str',
            'security_domain': 'str',
            'user_id': 'str',
            'user_name': 'str',
            'x_frame_options': 'str',
            'x_frame_options_allow_from_url': 'str'
        }

        self.attribute_map = {
            'assertion_id': 'assertionId',
            'authentication_instant': 'authenticationInstant',
            'authentication_method': 'authenticationMethod',
            'client_user_id': 'clientUserId',
            'email': 'email',
            'ping_frequency': 'pingFrequency',
            'ping_url': 'pingUrl',
            'recipient_id': 'recipientId',
            'return_url': 'returnUrl',
            'security_domain': 'securityDomain',
            'user_id': 'userId',
            'user_name': 'userName',
            'x_frame_options': 'xFrameOptions',
            'x_frame_options_allow_from_url': 'xFrameOptionsAllowFromUrl'
        }

        self._assertion_id = assertion_id
        self._authentication_instant = authentication_instant
        self._authentication_method = authentication_method
        self._client_user_id = client_user_id
        self._email = email
        self._ping_frequency = ping_frequency
        self._ping_url = ping_url
        self._recipient_id = recipient_id
        self._return_url = return_url
        self._security_domain = security_domain
        self._user_id = user_id
        self._user_name = user_name
        self._x_frame_options = x_frame_options
        self._x_frame_options_allow_from_url = x_frame_options_allow_from_url

    @property
    def assertion_id(self):
        """
        Gets the assertion_id of this RecipientViewRequest.
        A unique identifier of the authentication event executed by the client application.

        :return: The assertion_id of this RecipientViewRequest.
        :rtype: str
        """
        return self._assertion_id

    @assertion_id.setter
    def assertion_id(self, assertion_id):
        """
        Sets the assertion_id of this RecipientViewRequest.
        A unique identifier of the authentication event executed by the client application.

        :param assertion_id: The assertion_id of this RecipientViewRequest.
        :type: str
        """

        self._assertion_id = assertion_id

    @property
    def authentication_instant(self):
        """
        Gets the authentication_instant of this RecipientViewRequest.
        A sender generated value that indicates the date/time that the signer was authenticated.

        :return: The authentication_instant of this RecipientViewRequest.
        :rtype: str
        """
        return self._authentication_instant

    @authentication_instant.setter
    def authentication_instant(self, authentication_instant):
        """
        Sets the authentication_instant of this RecipientViewRequest.
        A sender generated value that indicates the date/time that the signer was authenticated.

        :param authentication_instant: The authentication_instant of this RecipientViewRequest.
        :type: str
        """

        self._authentication_instant = authentication_instant

    @property
    def authentication_method(self):
        """
        Gets the authentication_method of this RecipientViewRequest.
        A sender created value that indicates the convention used to authenticate the signer. This information is included in the Certificate of Completion.

        :return: The authentication_method of this RecipientViewRequest.
        :rtype: str
        """
        return self._authentication_method

    @authentication_method.setter
    def authentication_method(self, authentication_method):
        """
        Sets the authentication_method of this RecipientViewRequest.
        A sender created value that indicates the convention used to authenticate the signer. This information is included in the Certificate of Completion.

        :param authentication_method: The authentication_method of this RecipientViewRequest.
        :type: str
        """

        self._authentication_method = authentication_method

    @property
    def client_user_id(self):
        """
        Gets the client_user_id of this RecipientViewRequest.
        A sender created value that shows the recipient is embedded (captive).   Maximum length: 100 characters.

        :return: The client_user_id of this RecipientViewRequest.
        :rtype: str
        """
        return self._client_user_id

    @client_user_id.setter
    def client_user_id(self, client_user_id):
        """
        Sets the client_user_id of this RecipientViewRequest.
        A sender created value that shows the recipient is embedded (captive).   Maximum length: 100 characters.

        :param client_user_id: The client_user_id of this RecipientViewRequest.
        :type: str
        """

        self._client_user_id = client_user_id

    @property
    def email(self):
        """
        Gets the email of this RecipientViewRequest.
        Specifies the email of the recipient. You can use either email and userName or userId to identify the recipient.

        :return: The email of this RecipientViewRequest.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this RecipientViewRequest.
        Specifies the email of the recipient. You can use either email and userName or userId to identify the recipient.

        :param email: The email of this RecipientViewRequest.
        :type: str
        """

        self._email = email

    @property
    def ping_frequency(self):
        """
        Gets the ping_frequency of this RecipientViewRequest.
        Only used if pingUrl is specified. This is the interval, in seconds, between pings on the pingUrl.  The default is 300 seconds. Valid values are 60-1200 seconds.

        :return: The ping_frequency of this RecipientViewRequest.
        :rtype: str
        """
        return self._ping_frequency

    @ping_frequency.setter
    def ping_frequency(self, ping_frequency):
        """
        Sets the ping_frequency of this RecipientViewRequest.
        Only used if pingUrl is specified. This is the interval, in seconds, between pings on the pingUrl.  The default is 300 seconds. Valid values are 60-1200 seconds.

        :param ping_frequency: The ping_frequency of this RecipientViewRequest.
        :type: str
        """

        self._ping_frequency = ping_frequency

    @property
    def ping_url(self):
        """
        Gets the ping_url of this RecipientViewRequest.
        A client Url to be pinged by the DocuSign Signing experience to indicate to the client that Signing is active. An HTTP Get is executed against the client. The response from the client is ignored. The intent is for the client to reset it's session timer when the request is received.

        :return: The ping_url of this RecipientViewRequest.
        :rtype: str
        """
        return self._ping_url

    @ping_url.setter
    def ping_url(self, ping_url):
        """
        Sets the ping_url of this RecipientViewRequest.
        A client Url to be pinged by the DocuSign Signing experience to indicate to the client that Signing is active. An HTTP Get is executed against the client. The response from the client is ignored. The intent is for the client to reset it's session timer when the request is received.

        :param ping_url: The ping_url of this RecipientViewRequest.
        :type: str
        """

        self._ping_url = ping_url

    @property
    def recipient_id(self):
        """
        Gets the recipient_id of this RecipientViewRequest.
        Unique for the recipient. It is used by the tab element to indicate which recipient is to sign the Document.

        :return: The recipient_id of this RecipientViewRequest.
        :rtype: str
        """
        return self._recipient_id

    @recipient_id.setter
    def recipient_id(self, recipient_id):
        """
        Sets the recipient_id of this RecipientViewRequest.
        Unique for the recipient. It is used by the tab element to indicate which recipient is to sign the Document.

        :param recipient_id: The recipient_id of this RecipientViewRequest.
        :type: str
        """

        self._recipient_id = recipient_id

    @property
    def return_url(self):
        """
        Gets the return_url of this RecipientViewRequest.
        The url the recipient is redirected to after the signing session has ended. DocuSign redirects to the url and includes an event parameter that can be used by your application. Possible event parameter values:   * cancel (recipient canceled the signing operation) * decline (recipient declined to sign) * exception (an exception occurred) * fax_pending (recipient has a fax pending) * session_timeout (session timed out) * signing_complete (signer completed the signing ceremony) * ttl_expired (the TTL, time to live, timer expired) * viewing_complete (recipient completed viewing the envelope)  ###### Note: Include https:// in the URL or the redirect might not succeed on some browsers. 

        :return: The return_url of this RecipientViewRequest.
        :rtype: str
        """
        return self._return_url

    @return_url.setter
    def return_url(self, return_url):
        """
        Sets the return_url of this RecipientViewRequest.
        The url the recipient is redirected to after the signing session has ended. DocuSign redirects to the url and includes an event parameter that can be used by your application. Possible event parameter values:   * cancel (recipient canceled the signing operation) * decline (recipient declined to sign) * exception (an exception occurred) * fax_pending (recipient has a fax pending) * session_timeout (session timed out) * signing_complete (signer completed the signing ceremony) * ttl_expired (the TTL, time to live, timer expired) * viewing_complete (recipient completed viewing the envelope)  ###### Note: Include https:// in the URL or the redirect might not succeed on some browsers. 

        :param return_url: The return_url of this RecipientViewRequest.
        :type: str
        """

        self._return_url = return_url

    @property
    def security_domain(self):
        """
        Gets the security_domain of this RecipientViewRequest.
        The domain in which the user authenticated.

        :return: The security_domain of this RecipientViewRequest.
        :rtype: str
        """
        return self._security_domain

    @security_domain.setter
    def security_domain(self, security_domain):
        """
        Sets the security_domain of this RecipientViewRequest.
        The domain in which the user authenticated.

        :param security_domain: The security_domain of this RecipientViewRequest.
        :type: str
        """

        self._security_domain = security_domain

    @property
    def user_id(self):
        """
        Gets the user_id of this RecipientViewRequest.
        Specifies the user ID of the recipient. You can use with user ID or email and user name to identify the recipient. If user ID is used and a client user ID is provided, the value in the `userId` property must match a recipient ID (which can be retrieved with a GET recipients call) for the envelope. If a user ID is used and a clientUser ID is not provided, the user ID match the user ID of the authenticating user.

        :return: The user_id of this RecipientViewRequest.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this RecipientViewRequest.
        Specifies the user ID of the recipient. You can use with user ID or email and user name to identify the recipient. If user ID is used and a client user ID is provided, the value in the `userId` property must match a recipient ID (which can be retrieved with a GET recipients call) for the envelope. If a user ID is used and a clientUser ID is not provided, the user ID match the user ID of the authenticating user.

        :param user_id: The user_id of this RecipientViewRequest.
        :type: str
        """

        self._user_id = user_id

    @property
    def user_name(self):
        """
        Gets the user_name of this RecipientViewRequest.
        Specifies the username of the recipient. You can use either email and userName or userId to identify the recipient.

        :return: The user_name of this RecipientViewRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this RecipientViewRequest.
        Specifies the username of the recipient. You can use either email and userName or userId to identify the recipient.

        :param user_name: The user_name of this RecipientViewRequest.
        :type: str
        """

        self._user_name = user_name

    @property
    def x_frame_options(self):
        """
        Gets the x_frame_options of this RecipientViewRequest.
        

        :return: The x_frame_options of this RecipientViewRequest.
        :rtype: str
        """
        return self._x_frame_options

    @x_frame_options.setter
    def x_frame_options(self, x_frame_options):
        """
        Sets the x_frame_options of this RecipientViewRequest.
        

        :param x_frame_options: The x_frame_options of this RecipientViewRequest.
        :type: str
        """

        self._x_frame_options = x_frame_options

    @property
    def x_frame_options_allow_from_url(self):
        """
        Gets the x_frame_options_allow_from_url of this RecipientViewRequest.
        

        :return: The x_frame_options_allow_from_url of this RecipientViewRequest.
        :rtype: str
        """
        return self._x_frame_options_allow_from_url

    @x_frame_options_allow_from_url.setter
    def x_frame_options_allow_from_url(self, x_frame_options_allow_from_url):
        """
        Sets the x_frame_options_allow_from_url of this RecipientViewRequest.
        

        :param x_frame_options_allow_from_url: The x_frame_options_allow_from_url of this RecipientViewRequest.
        :type: str
        """

        self._x_frame_options_allow_from_url = x_frame_options_allow_from_url

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
