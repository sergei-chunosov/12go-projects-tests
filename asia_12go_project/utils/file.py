def abs_path_from_project(relative_path: str):
    import asia_12go_project.utils
    from pathlib import Path

    return (
        Path(asia_12go_project.utils.__file__)
            .parent.parent.parent.joinpath(relative_path)
            .absolute()
            .__str__()
    )
