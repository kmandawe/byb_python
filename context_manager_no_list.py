from multiple_context_manager import nest_test

# with [nest_test('a'), nest_test('b')]:
#     pass

with nest_test('a'), nest_test('b'):
    pass

with nest_test('a'), \
     nest_test('b'), \
     nest_test('c'):
    pass
