from Plugins.Plugin import PluginDescriptor

def main(session, **kwargs):
    import os
    os.system('mkdir -p /tmp/ofwlauncher')
    os.system('mount /dev/sda1 /tmp/ofwlauncher')
    os.system('sync; sleep 2')
    os.system('[ -f /tmp/ofwlauncher/vmlinux ] && [ -f /tmp/ofwlauncher/kexec ] && /tmp/ofwlauncher/kexec -f /tmp/ofwlauncher/vmlinux')
    os.system('[ -f /tmp/ofwlauncher/vmlinux ] && [ -f /tmp/ofwlauncher/kexecofw ] && /tmp/ofwlauncher/kexecofw -f /tmp/ofwlauncher/vmlinux')


def startSetup(menuid):
    if menuid == 'shutdown':
        return [(_('OFW Launcher'),
          main,
          'ofw_launcher',
          None)]
    print 'menuid =  %s' % menuid
    return []


def Plugins(**kwargs):
    return [PluginDescriptor(name=_('OFW Launcher'), description=_('Launches Original Firmware using USB'), where=PluginDescriptor.WHERE_MENU, needsRestart=False, fnc=startSetup)]
