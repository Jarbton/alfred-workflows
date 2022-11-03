# alfred-workflows
A repo for maintaining Alfred 5 workflows.

The majority of the workflows are Python variations of [rknightuk's JavaScript alfred-workflows](https://github.com/rknightuk/alfred-workflows).

## Workflows
### Text Transform - [Download v1.0.2](workflows/text_transform/text_transform.alfredworkflow)

Transform provided text to various cases.

![text_transform screenshot](workflows/text_transform/src/text_transform_screenshot.png)


#### Usage
- Keyword: `tt`
- Choose a case from the list.
- Hold `⌘` to copy the result to the clipboard.




### Monzo Link Generator - [Download v1.0.4](workflows/monzo/monzo.alfredworkflow)

Generate Monzo.me link providing cost and description.

![monzo-link-generator screenshot](workflows/monzo/src/monzo_screenshot.png)

#### Usage
- Keyword: `monzo`
- First arg - cost
- Second arg - description


## Dev Setup
### Prerequisites
- [Poetry](https://python-poetry.org/docs/#installation)

### Installing Dependencies
```bash
Poetry install
```

### Running Unit Tests
```bash
Poetry run pytest
```