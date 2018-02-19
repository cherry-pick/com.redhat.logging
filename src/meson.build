com_redhat_logging_sources = files('''
        main.c
        util.h
'''.split())

com_redhat_logging_varlink_c_inc = custom_target(
        'com.redhat.logging.varlink',
        input : 'com.redhat.logging.varlink',
        output : 'com.redhat.logging.varlink.c.inc',
        command : [varlink_wrapper_py, '@INPUT@', '@OUTPUT@'])

exe = executable(
        'com.redhat.logging',
        com_redhat_logging_sources,
        com_redhat_logging_varlink_c_inc,
        dependencies : [
                libvarlink,
                libsystemd
        ],
        install : true)
