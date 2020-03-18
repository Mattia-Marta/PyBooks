'''
Running a code using threads make it smarter to run.
Threading is make your sw run on different "lines" simultaneously.

To make a separate thread, a Thread obj need to be created using threading.Thread().
Look at the example named "ThreadDemo".

If the target function you want to run in the new thread takes arguments, 
you can pass the target function’s arguments to threading.Thread().
To make the "Arguments passing with threads" possible with threads, the args
can be specified as a dictionary to the kwargs keyword argument.

One of the biggest issue possible with threads is concurrency, a scenario created from
2 threads asking or trying to use the same resource.
'''

#ThreadDemo: The print of "Wake up!" happens after the "End of program" one, beacuse of threads

print('Start of program.')
def takeANap():    
    time.sleep(5)    
    print('Wake up!') 

threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('End of program.')


#Arguments passing with threads:
>>>print('Cats', 'Dogs', 'Frogs', sep=' & ')
Cats & Dogs & Frogs

#With threads:
threadObj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep': ' & '})
>>> threadObj.start()
Cats & Dogs & Frogs

