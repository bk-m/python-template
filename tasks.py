"""
Run tasks by activating the environment, followed by `inv <task_name>`.
"""

from invoke import Context, task


@task
def run(ctx: Context) -> None:
    """
    Run `main.py`.

    Args:
        ctx (Context): Invoke's context
    """
    ctx.run("python ./app/main.py")


@task
def lint(ctx: Context) -> None:
    """
    Run static code analysis.

    Args:
        ctx (Context): Invoke's context
    """
    ctx.run(
        # Ignore UP034.
        (
            "echo MyPy: && mypy . && echo Black: && black ./app ./tests && "
            "echo Ruff: && ruff ./app ./tests"
        ),
    )


@task
def test(ctx: Context) -> None:
    """
    Run `pytest`.

    Args:
        ctx (Context): Invoke's context
    """
    ctx.run("pytest")
