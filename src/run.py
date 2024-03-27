import click
import utils

@click.command()
@click.option('--name', prompt='Project Name', help='The name of your project and folder')
@click.option('--tailwind', default="n", prompt='Do you want to use tailwind', help='Do you wan to use the css framework tailwind, which use utility classes')
@click.option('--basic', is_flag=True, default=False, help='Sets up a basic blueprint routed layout returning "Hello, World!"')
@click.option('--api', is_flag=True, default=False, help='Adds a blueprint for API route handling')
@click.option('--basic-api', is_flag=True, default=False, help='Adds blueprints for API and Views for route handling')
@click.option('--flask-admin', is_flag=True, default=False, help='Sets up a flask-admin app from the official GitHub repo')
@click.option('--port', default=80, help='The port the webserver will be hosted on')
@click.option('--debug', is_flag=True, default=False, help='Allow jinja to auto reload when developing')
@click.option('--host', default="0.0.0.0", help='The way Flask listens to incoming requests')
@click.option('--secret-key', default="random", help='The way Flask listens to incoming requests')
@click.option('--site-name', default="Flask Site", help='The name of your site, not required')
@click.option('--layout', is_flag=True, default=False, help='Adds a layout.html to the templates and references it in index.html')

def project(name: str, tailwind: bool, basic: bool, api: bool, basic_api: bool, flask_admin: bool, port: int = 80, debug: bool = True, host: str = "0.0.0.0", secret_key: str = "random", site_name: str = "Flask Site", layout: bool = False) -> None:
    if site_name:
        project_name = site_name
    else:
        project_name = name

    name = utils.path(name)

    project = None

    use_tailwind = tailwind

    if basic:
        project = "basic"
        if tailwind:
            use_tailwind = True
    elif api:
        project = "api"
        if tailwind:
            use_tailwind = False
    elif basic_api:
        project = "basic-api"
        if tailwind:
            use_tailwind = True
    elif flask_admin:
        project = "flask-admin"
        if tailwind:
            use_tailwind = False
    else:
        project = "basic"
        if tailwind:
            use_tailwind = True

    if project:
        utils.copy_tree(f"utils/examples/{project}", name, project)
        utils.create_config(name, port, host, debug, secret_key, project_name, project)
        utils.append_after(name, layout, project)

        if use_tailwind:
            utils.install_tailwind(name)

if __name__ == "__main__":
    project() 