import click
import utils

@click.command()
@click.option('--name', prompt='Project Name', help='The name of your project and folder')
@click.option('--tailwind', default=False, is_flag=True, prompt='Do you want to use tailwind', help='Do you want to use the css framework tailwind, which uses utility classes')
@click.option('--basic', is_flag=True, default=False, help='Sets up a basic blueprint routed layout returning "Hello, World!"')
@click.option('--api', is_flag=True, default=False, help='Adds a blueprint for API route handling')
@click.option('--basic-api', is_flag=True, default=False, help='Adds blueprints for API and Views for route handling')
@click.option('--flask-admin', is_flag=True, default=False, help='Sets up a flask-admin app from the official GitHub repo')
@click.option('--port', default=80, help='The port the webserver will be hosted on')
@click.option('--debug', is_flag=True, default=False, help='Allow Jinja to auto-reload when developing')
@click.option('--host', default="0.0.0.0", help='The way Flask listens to incoming requests')
@click.option('--secret-key', default="random", help='The way Flask listens to incoming requests')
@click.option('--site-name', default="Flask Site", help='The name of your site, not required')
@click.option('--layout', is_flag=True, default=False, help='Adds a layout.html to the templates and references it in index.html')
def project(name, tailwind, basic, api, basic_api, flask_admin, port=80, debug=False, host="0.0.0.0", secret_key="random", site_name="Flask Site", layout=False):
    project_name = site_name if site_name else name
    project_type = None

    if basic:
        project_type = "basic"
    elif api:
        project_type = "api"
    elif basic_api:
        project_type = "basic-api"
    elif flask_admin:
        project_type = "flask-admin"
    else:
        project_type = "basic"

    use_tailwind = tailwind and (basic or basic_api)

    utils.copy_tree(f"utils/examples/{project_type}", utils.path(name), project_type)
    utils.create_config(name, port, host, debug, secret_key, project_name, project_type)
    utils.append_after(name, layout, project_type)

    if use_tailwind:
        utils.install_tailwind(name)

if __name__ == "__main__":
    project()