from rich.progress import (
    Progress,
    BarColumn,
)


def progress_task(task_title, task_list, action):
    length = len(task_list)

    with Progress(
        "[bold magenta]{task.description}",
        BarColumn(bar_width=30),
        "[progress.percentage]{task.percentage:>3.0f}%",
    ) as progress:
        task = progress.add_task(task_title, total=length)

        for t in task_list:
            action(t)
            progress.update(task, advance=1)
