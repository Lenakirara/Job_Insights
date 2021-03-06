from .jobs import read


# refatorando - usando set() - buscando valores unicos
def get_unique_job_types(path):
    jobs_csv = read(path)
    jobs_types_list = set()
    for job in jobs_csv:
        if job["job_type"] not in jobs_types_list:
            jobs_types_list.add(job["job_type"])
    return jobs_types_list


# refatorado - usando list comprehension
# https://pythonacademy.com.br/blog/list-comprehensions-no-python
def filter_by_job_type(jobs, job_type):
    job_type_list = [
        job for job in jobs
        if job["job_type"] == job_type
    ]
    return job_type_list


# SET: https://www.w3schools.com/python/ref_func_set.asp
# ADD: https://www.w3schools.com/python/ref_set_add.asp
# usando set() para pegar valores unicos
# usando ADD pois funciona com set(), pois append() não funciona.
def get_unique_industries(path):
    jobs_csv = read(path)
    industry_list = set()
    for job in jobs_csv:
        if job["industry"] != "":
            industry_list.add(job["industry"])
    return industry_list


# refatorado - usando list comprehension
# https://pythonacademy.com.br/blog/list-comprehensions-no-python
def filter_by_industry(jobs, industry):
    job_industry_list = [
        job for job in jobs
        if job["industry"] == industry
    ]
    return job_industry_list


# refatorando - usando isdigit() - vendo documentação:
# retorna true se os caracteres na string forem digitos.
# além do erro: ValueError: invalid literal for int() with base 10: 'invalid'
# isdigt() seria mais usual que o isnumeric()
# https://docs.python.org/3/library/stdtypes.html?highlight=isdigit
def get_max_salary(path):
    jobs_csv = read(path)
    max_salary = 0
    for job in jobs_csv:
        if job["max_salary"].isdigit():
            if int(job["max_salary"]) > max_salary:
                max_salary = int(job["max_salary"])
    return max_salary


# inicializando o min_salary com 0 não passa no teste
# Inicializando com valor que vem em max_salary é possivel fazer a comparação
# e verificar menor valor.
def get_min_salary(path):
    jobs_csv = read(path)
    min_salary = get_max_salary(path)
    for job in jobs_csv:
        if job["min_salary"].isdigit():
            if int(job["min_salary"]) < min_salary:
                min_salary = int(job["min_salary"])
    return min_salary


# refatorando condicional - retirando excesso de if
def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("Values doesn't exists")

    min_salary = job["min_salary"]
    max_salary = job["max_salary"]

    if (
        type(min_salary) is not int
        or type(min_salary) is not int
        or type(salary) is not int
    ):
        raise ValueError("Some value entered is not an integer")
    elif min_salary > max_salary:
        raise ValueError("Min. salary is greather than Max. salary")
    return min_salary <= salary <= max_salary


def filter_by_salary_range(jobs, salary):
    job_salary_range = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                job_salary_range.append(job)
        except ValueError:
            pass
    return job_salary_range
