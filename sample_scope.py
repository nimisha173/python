
def check_scope():
    def do_local():
        test="locat test"
    def non_local():
        nonlocal test
        # local value
        test="non local test"
    def do_global():
        # in the case of global that will print non local test because that call will affect on just above the function
        global test
        test="global test"
    # global value
    test="default"
    do_local()
    print("test value after do_local:"+test)
    non_local()
    print("test value after do_non_local:"+test)
    do_global()
    print("test value after do_global:"+test)
check_scope()

print("test value after main:"+test)
# after the main function the current value of test will print that is global test
