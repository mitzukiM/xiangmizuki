body_parts = ['arm','hand','head']
def uses_the_word(part):
    for hand in body_parts:
        if 'hand' in body_parts:
            return True
        if 'hand' not in body_parts:
            return False
        break

check  =uses_the_word(part = 'hand')
print(check )


