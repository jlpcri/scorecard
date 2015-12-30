from django.contrib import admin

from models import ProductQualityIndividual, PQProjects, PQInitiatives,\
    QualityAssuranceIndividual, QAProjects, QAInitiatives,\
    TestEngineeringIndividual, TEProjects, TEInitiatives,\
    RequirementsEngineeringIndividual, QualityInnovationIndividual, TestLabIndividual,\
    Projects, DefiningObjectives


for m in [ProductQualityIndividual, PQProjects, PQInitiatives,
          QualityAssuranceIndividual, QAProjects, QAInitiatives,
          TestEngineeringIndividual, TEProjects, TEInitiatives,
          # RequirementsEngineeringIndividual, QualityInnovationIndividual, TestLabIndividual,
          Projects, DefiningObjectives
          ]:
    admin.site.register(m)
