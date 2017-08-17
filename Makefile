clean:
	rm -rf build dist
	find . -name '*.pyc' -exec rm \{\} \;

test:
	openfisca-run-test openfisca_extension_template/tests --country_package openfisca_country_template --extensions openfisca_extension_template
