io_systemd_journal_sources = files('''
        main.c
        util.h
'''.split())

io_systemd_journal_varlink_c_inc = custom_target(
        'io.systemd.journal.varlink',
        input : 'io.systemd.journal.varlink',
        output : 'io.systemd.journal.varlink.c.inc',
        command : [varlink_wrapper_py, '@INPUT@', '@OUTPUT@'])

exe = executable(
        'io.systemd.journal',
        io_systemd_journal_sources,
        io_systemd_journal_varlink_c_inc,
        dependencies : [
                libvarlink,
                libsystemd
        ],
        install : true)
