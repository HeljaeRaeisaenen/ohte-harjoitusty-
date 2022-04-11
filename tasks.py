from invoke import task

@task
def foo(ctx):
    print("bar")

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

@task
def test(ctx):
    ctx.run("pytest src &&  coverage run --branch -m pytest src && coverage report -m", pty=True)
   
@task
def coverage_report(ctx):
    ctx.run("pytest src && coverage run --branch -m pytest src && coverage html")

@task
def coverage_html(ctx):
    ctx.run("xdg-open '/home/raisaneh/k/ohte/ohte_harjo/htmlcov/index.html'")

@task
def lint(ctx):
    ctx.run("pylint src")

@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src")
