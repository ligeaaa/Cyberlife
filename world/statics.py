from entity.base_module.base_statics import BaseStatics


class DeathAndBreedStatics(BaseStatics):
    borned = 0
    death = 0

    def __str__(self):
        return f"Born: {self.borned}\nDeath: {self.death}"