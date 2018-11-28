# Changelog

### 1.2.0 - [#18](https://github.com/openfisca/extension-template/pull/18)

* Technical change
* Details:
  - Adapt to Core v25

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
