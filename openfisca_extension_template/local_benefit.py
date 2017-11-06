# -*- coding: utf-8 -*-
from __future__ import division

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_country_template.entities import *


class local_town_child_allowance(Variable):
    value_type = float
    entity = Household
    definition_period = MONTH
    label = u"Local benefit: a fixed amount by child each month"

    def formula(famille, period, parameters):
        nb_children = famille.nb_persons(role = Household.CHILD)
        amount_by_child = parameters(period).local_town.child_allowance.amount

        return nb_children * amount_by_child
