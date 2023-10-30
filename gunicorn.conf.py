workers = 2

bind = 'unix:/home/dlr/courseRecoSystem/courseRecoSystem.sock'

worker_class = 'sync'

timeout = 2880

accesslog = '-'

app = 'courseRecoSystem.wsgi:application'