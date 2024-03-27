# Flask-Setup
A simple CLI tool to quickly initialize a Flask project with multiple options and frameworks

## Installation

Install Flask-Setup using GIT

```bash
git clone "https://github.com/jackablett/Flask-Setup.git" "flask-setup"
cd "flask-setup/src"
pip install -r requirements.txt
```

(use correct version of pip and python according to your OS and python install)

## Get Started

```bash
python run.py [params]
```
### Params

These parameters can be passed in via tags in the command line

To create a route with a basic "index" page which returns "Hello, World!"
```bash
python run.py --basic
```

- Name (required)
- Tailwind (required)
- Basic
- Api
- Basic-Api
- Flask-admin (seperate singular app)
- Port
- Debug
- Host
- Secret-key
- Site-name
- Layout

## Tag Meaning

### Name
```
--name
```
The name tag is the project name including the folder creation.

### Tailwind
```
--tailwind
```
If tailwind is equal to "y" or true, tailwindcss will be installed. For more details visit the official [Tailwind installation guide](https://tailwindcss.com/docs/installation).

### Basic
```
--basic
```
This tag creates a basic boilerplate Flask site with a simple index page that returns "Hello, World!"

### Api
```
--api
```
This tag creates a basic boilerplate Flask site with a simple api route page returning "Hello, World!" as JSON.

### Basic-Api
```
--basic-api
```
This tag creates a site with an index route returning "Hello, World!" also including an Api blueprint, which allows developers to create an Api controlled frontend with a framework like [JQuery](https://jquery.com/) or [Vue](https://vuejs.org/).

### Flask-Admin
```
--flask-admin
```
Flask-Admin creates a standard Flask-Admin app taken from the Flask-Admin GitHub, meaning it won't have tailwindcss support YET similary with the seperate Api and Basic routes.

### Port
```
--port [port-number]
```
This port tag allows developers to suggest the web server port, by default setting to port 80.

### Debug
```bash
--debug
```
Enabling debug mode allows developers to run the Flask application in debug mode, which provides additional information and enables features like automatic code reloading.

### Host
```bash
--host [host-address]
```
Specifies the host address for the Flask application. By default, Flask binds to localhost (127.0.0.1), but developers can specify a different IP address if needed.

### Secret-key
```bash
--secret-key [your-secret-key]
```
Sets the secret key for the Flask application. This key is used for securely signing session cookies and other security-related functionality. It's important to use a strong, random secret key to prevent security vulnerabilities.

### Site-name
```bash
--site-name [your-site-name]
```
Specifies the name of the Flask project or website. This can be useful for generating default page titles, headers, or other site-specific content.

### Layout
```bash
--layout [layout-name]
```
Defines the layout or template structure for the Flask project. This could refer to different HTML/CSS frameworks or custom layouts. Implementing different layouts allows for flexibility in the project's design and structure.

## Bugs?
If you notice any bugs or would like a new featue, please create an issue or pull request, cheers.