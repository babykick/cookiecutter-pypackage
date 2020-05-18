import argparse

import click

# from .core import xxx

#-- Use argparse --#

# def _argparse():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('url', nargs='?', help='target playlist url')
#     parser.add_argument('--listfile', help='file containing video links')
#     parser.add_argument('--savedir', default=cur_dir, help='directory downloaded video saved')
#     parser.add_argument('--useindex', action='store_true', help='use index or not in format')
#     parser.add_argument('--displayid', action='store_true', help='add display id in output template')
    
#     return parser.parse_args()
# args = _argparse()


#-- Use click --#

@click.command()
@click.argument('arg1')
@click.option('-o', '--opt1', default='', help='...', )
def main(arg1, opt1):
    """Console script for {{cookiecutter.project_slug}}"""
    click.echo("Replace this message by putting your code into "
               "{{cookiecutter.project_slug}}.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")


if __name__ == "__main__":
    main()
