def run():
    country_population = {
	   'Argentina': 44_938_712,
	   'Brasil': 210_147_125,
	   'Colombia': 50_372_424
    }
    for country, population in country_population.items():
        print(f'{country} has {population} of population')


if __name__ == "__main__":
    run()
