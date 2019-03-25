# Changelog

## 1.3.0

* Technical change
* Details:
  - Remove Python 2 build and deploy on continuous integration
  - Update test command
  - Update `country-template` dependency (uses Core v27)


### 1.2.0 - [#18](https://github.com/openfisca/extension-template/pull/18)

* Technical change
* Details:
  - Adapt to OpenFisca Core v25
  - Change the syntax of OpenFisca YAML tests

For instance, a test that was using the `input_variables` and the `output_variables` keywords like:

```yaml
- name: Basic income
  period: 2016-12
  input_variables:
    salary: 1200
  output_variables:
    basic_income: 600
```

becomes:

```yaml
- name: Basic income
  period: 2016-12
  input:
    salary: 1200
  output:
    basic_income: 600
```

A test that was fully specifying its entities like:

```yaml
- name: "A couple with 2 children gets 200€"
  period: 2016-01
  households:
    parents: ["parent1", "parent2"]
    children: ["child1", "child2"]
  persons:
  - id: "parent1"
    age: 35
  - id: "parent2"
    age: 35
  - id: "child1"
    age: 8
  - id: "child2"
    age: 4
  output_variables:
    local_town_child_allowance: 200
```

becomes:

```yaml
- name: "A couple with 2 children gets 200€"
  period: 2016-01
  input:
    households:
      household:
        parents: ["parent1", "parent2"]
        children: ["child1", "child2"]
    persons:
      parent1:
        age: 35
      parent2:
        age: 35
      child1:
        age: 8
      child2:
        age: 4
  output:
    local_town_child_allowance: 200
```

### 1.1.7 - [#16](https://github.com/openfisca/extension-template/pull/16)

* Technical change
* Details:
  - Tests library against its packaged version
  - By doing so, we prevent some hideous bugs

### 1.1.6 - [#15](https://github.com/openfisca/extension-template/pull/15)

_Note: the 1.1.5 version has been unpublished as it was used for test analysis_

* Add continuous deployment with CircleCI, triggered by a merge to `master` branch

### 1.1.4 - [#13](https://github.com/openfisca/extension-template/pull/13)

* Declare package compatible with OpenFisca Country Template v3

## 1.1.3 - [#8](https://github.com/openfisca/extension-template/pull/8)

* Technical improvement:
* Details:
  - Adapt to version `21.0.0` of Openfisca-Core and version `2.1.0` of Country-Template

## 1.1.2 - [#7](https://github.com/openfisca/extension-template/pull/7)

* Technical improvement:
* Details:
  - Adapt to version `20.0.0` of Openfisca-Core and version `1.4.0` of Country-Template

## 1.1.1 - [#5](https://github.com/openfisca/extension-template/pull/5)

* Technical improvement: adapt to version `17.0.0` of Openfisca-Core and version `1.2.4` of Country-Template
* Details:
  - Transform XML parameter files to YAML parameter files.
  - Gather tests in the directory `tests`. The command `make test` runs only the tests contained in that directory.
  - Add a changelog.
