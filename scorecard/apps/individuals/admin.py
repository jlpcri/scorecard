from django.contrib import admin

from models import ProductQualityIndividual, PQProjects, PQInitiatives,\
    QualityAssuranceIndividual, QAProjects, QAInitiatives,\
    TestEngineeringIndividual, TEProjects, TEInitiatives,\
    RequirementsEngineeringIndividual, QualityInnovationIndividual, TestLabIndividual


for m in [ProductQualityIndividual, PQProjects, PQInitiatives,
          QualityAssuranceIndividual, QAProjects, QAInitiatives,
          TestEngineeringIndividual, TEProjects, TEInitiatives,
          RequirementsEngineeringIndividual, QualityInnovationIndividual, TestLabIndividual
          ]:
    admin.site.register(m)
