# OpenFisca Extension-Template

This repository is here to help you install your own OpenFisca [extension](https://doc.openfisca.fr/contribute/extensions.html) package.

## Installing

> We assume that you have already installed your own OpenFisca country package. If you don't have such a package in your environment, see OpenFisca [documentation](https://doc.openfisca.fr/coding-the-legislation/bootstrapping_a_new_country_package.html) for more information.

> We recommend that you [use a virtualenv](https://doc.openfisca.fr/for_developers.html#create-a-virtualenv) to install OpenFisca. If you don't, you may need to add `--user` at the end of all commands starting by `pip`.

To install your extension, go to the directory where you want to install it. Then, follow these steps:
1. Download this template code and move into its directory: 

```
git clone https://github.com/openfisca/openfisca-extension-template.git
cd openfisca-extension-template
```

2. Look for the name of your country package:
* If you are using `openfisca_country_template`, you are all set. Follow the next step.
* If you want to use a specific country package, open the [Makefile](./Makefile) and replace `openfisca_country_template` by your country package name in:

  `openfisca-run-test openfisca_extension_template --country_package `**`openfisca_country_template`**` --extensions openfisca_extension_template`

3. Run:

```
pip install -e ".[test]"
```

You can make sure that everything is working by running the provided tests:

```sh
make test
```

> [Learn more about tests](https://doc.openfisca.fr/coding-the-legislation/writing_yaml_tests.html).

Your extension package is now installed and ready!
