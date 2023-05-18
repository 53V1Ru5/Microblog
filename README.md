# Microblog-react-flask

- bootstrap: a CSS user interface library for web pages.
- react-bootstrap: a React component library wrapper for the bootstrap package.
- react-router-dom: a React component library that implements client-side routing.
- serve: a static file web server that can be used to run the production version of the React application.

# Welcome to the documentation for the Microblog API\!

This project is written in Python, with
the [<span class="underline">Flask</span>](https://flask.palletsprojects.com/) web
framework. 

Microblog-API is an easy to use web API for creating microblogs. It is
an ideal project to use when learning a front end framework, as it
provides a fully implemented back end that you can integrate against.

Microblog API provides all the base features required to implement a
microblogging project:

  - User registration, login and logout

  - Password recovery flow with reset emails

  - Post creation and deletion

  - Follow and unfollow users

  - Feed with posts from followed users

  - Pagination

  - Option to disable authentication during development

<table>
<thead>
<tr class="header">
<th>ENVIRONMENT VARIABLE</th>
<th>DEFAULT</th>
<th>DESCRIPTION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>SECRET_KEY</p>
</blockquote></td>
<td><blockquote>
<p>top-secret!</p>
</blockquote></td>
<td><blockquote>
<p>A secret key used when signing tokens.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DATABASE_URL</p>
</blockquote></td>
<td><blockquote>
<p>sqlite:///db.sqlite</p>
</blockquote></td>
<td><blockquote>
<p>The database URL, as defined by the <a href="https://docs.sqlalchemy.org/en/14/core/engines.html#database-urls"><span class="underline">SQLAlchemy</span></a> framework.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SQL_ECHO</p>
</blockquote></td>
<td><blockquote>
<p>not defined</p>
</blockquote></td>
<td><blockquote>
<p>Whether to echo SQL statements to the console for debugging purposes.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DISABLE_AUTH</p>
</blockquote></td>
<td><blockquote>
<p>not defined</p>
</blockquote></td>
<td><blockquote>
<p>Whether to disable authentication. When running with authentication disabled, the user is assumed to be logged as the user with id=1, which must exist in the database.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ACCESS_TOKEN_MINUTES</p>
</blockquote></td>
<td><blockquote>
<p>15</p>
</blockquote></td>
<td><blockquote>
<p>The number of minutes an access token is valid for.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>REFRESH_TOKEN_DAYS</p>
</blockquote></td>
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>The number of days a refresh token is valid for.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>REFRESH_TOKEN_IN_COOKIE</p>
</blockquote></td>
<td><blockquote>
<p>yes</p>
</blockquote></td>
<td><blockquote>
<p>Whether to return the refresh token in a secure cookie.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>REFRESH_TOKEN_IN_BODY</p>
</blockquote></td>
<td><blockquote>
<p>no</p>
</blockquote></td>
<td><blockquote>
<p>Whether to return the refresh token in the response body.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>RESET_TOKEN_MINUTES</p>
</blockquote></td>
<td><blockquote>
<p>15</p>
</blockquote></td>
<td><blockquote>
<p>The number of minutes a reset token is valid for.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PASSWORD_RESET_URL</p>
</blockquote></td>
<td><blockquote>
<p>http://localhost:3000/reset</p>
</blockquote></td>
<td><blockquote>
<p>The URL that will be used in password reset links.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>USE_CORS</p>
</blockquote></td>
<td><blockquote>
<p>yes</p>
</blockquote></td>
<td><blockquote>
<p>Whether to allow cross-origin requests. If allowed, CORS support can be configured or customized with options provided by the Flask-CORS extension.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DOCS_UI</p>
</blockquote></td>
<td><blockquote>
<p>elements</p>
</blockquote></td>
<td><blockquote>
<p>The UI library to use for the documentation. Allowed values are swagger_ui, redoc, rapidoc and elements.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MAIL_SERVER</p>
</blockquote></td>
<td><blockquote>
<p>localhost</p>
</blockquote></td>
<td><blockquote>
<p>The mail server to use for sending emails.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MAIL_PORT</p>
</blockquote></td>
<td><blockquote>
<p>25</p>
</blockquote></td>
<td><blockquote>
<p>The port to use for sending emails.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MAIL_USE_TLS</p>
</blockquote></td>
<td><blockquote>
<p>not defined</p>
</blockquote></td>
<td><blockquote>
<p>Whether to use TLS when sending emails.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MAIL_USERNAME</p>
</blockquote></td>
<td><blockquote>
<p>not defined</p>
</blockquote></td>
<td><blockquote>
<p>The username to use for sending emails.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MAIL_PASSWORD</p>
</blockquote></td>
<td><blockquote>
<p>not defined</p>
</blockquote></td>
<td><blockquote>
<p>The password to use for sending emails.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MAIL_DEFAULT_SENDER</p>
</blockquote></td>
<td><blockquote>
<p>donotreply@microblog.com</p>
</blockquote></td>
<td><blockquote>
<p>The default sender to use for emails.</p>
</blockquote></td>
</tr>
</tbody>
</table>

**<span class="underline">Configuration</span>**

If you are running Microblog API yourself while developing your front
end, there are a number of environment variables that you can set to
configure its behavior. The variables can be defined directly in the
environment or in a .env file in the project directory. The following
table lists all the environment variables that are currently used:

**<span class="underline">Authentication</span>**

The authentication flow for this API is based
on *access* and *refresh* tokens.

To obtain an access and refresh token pair, the client must send
a POST request to the /api/tokens endpoint, passing the username and
password of the user in a Authorization header, according to HTTP Basic
Authentication scheme. The response includes the access and refresh
tokens in the body. For added security in single-page applications, the
refresh token is also returned in a secure cookie.

Most endpoints in this API are authenticated with the access token,
passed in the Authorization header, using the Bearer scheme.

Access tokens are valid for 15 minutes (by default) from the time they
are issued. When the access token is expired, the client can renew it
using the refresh token. For this, the client must send a PUT request to
the /api/tokens endpoint, passing the expired access token in the body
of the request, and the refresh token either in the body, or through the
secure cookie sent when the tokens were requested. The response to this
request will include a new pair of tokens. Refresh tokens have a default
validity period of 7 days, and can only be used to renew the access
token they were returned with. An attempt to use a refresh token more
than once is considered a possible attack, and will cause all existing
tokens for the user to be revoked immediately as a mitigation measure.

All authentication failures are handled with a 401 status code in the
response.

**<span class="underline">Password
Resets</span>**

This API supports a password reset flow, to help users who forget their
passwords regain access to their accounts. To issue a password reset
request, the client must send a POST request to /api/tokens/reset,
passing the user's email in the body of the request. The user will
receive a password reset link by email, based on the password reset URL
entered in the configuration and a token query string paramter set to an
email reset token, with a validity of 15 minutes.

When the user clicks on the password reset link, the client application
must capture the token query string argument and send it in
a PUT request to /api/tokens/reset, along with the new password chosen
by the user.

**<span class="underline">Pagination</span>**

API endpoints that return collections of resources, such as the users or
posts, implement pagination, and the client must use query string
arguments to specify the range of items to return.

The number of items to return is specified by the limit argument, which
is optional. If not specified, the server sets the limit to a reasonable
value for the endpoint. If the limit is too large, the server may decide
to use a lower value instead. The following example shows how to request
the first 10 users:

http://localhost:5000/api/users?limit=10

The offset argument is used to specify the zero-based index of the first
item to return. If not given, the server sets the offset to 0. The
following example shows how to request the second page of users with a
page size of 10:

http://localhost:5000/api/users?limit=10\&offset=10

Sometimes paginating with the offset argument can be inconvenient, such
as with collections where new elements are not always inserted at the
end of the list. As an alternative to offset, the after argument can be
used to set the start item to the item after the one specified. This API
supports after for collections of blog posts, which are sorted by their
publication time in descending order, and for collections of users,
which are sorted by their username in ascending order. For blog posts,
the after argument must be set to a date and time specification in ISO
8601 format, such as 2020-01-01T00:00:00Z. For users, the after argument
must be set to a string. Examples:

http://localhost:5000/api/posts?limit=10\&after=2021-01-01T00:00:00

http://localhost:5000/api/users/me/followers?limit=10\&after=diana

The response body in a paginated request contains a data attribute that
is set to the list of entities that are in the requested page.
A pagination attribute is also included
with offset, limit, count and total sub-attributes, which should
enable the client to present pagination controls to the user.

**<span class="underline">Errors</span>**

All errors returned by this API use the following JSON structure:

{

"code": \<numeric error code\>,

"message": \<short error message\>,

"description": \<longer error description\>,

}

In the case of schema validation errors, an errors property is also
returned, containing a detailed list of validation errors found in the
submitted request:

{

"code": \<error code\>,

"message": \<error message\>,

"description": \<error description\>,

"errors": \[ \<error details\>, ... \]

}
