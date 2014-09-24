import Kernel


class EventCommandFormater(object):

    '''Formats event commands into HTML for display'''

    @staticmethod
    def formatCommand(command):
        formater = EventCommandFormater.get_event_formater(command.code).object
        if formater is None:
            return ''.join(
                (
                    EventHTMLFormater.indent(command.indent),
                    '<font color="red"><b>ERROR:</b> No Handeler for event code [%s]</font>' %
                    command.code
                )
            )
        text = formater.formatCommand(command.parameters)
        if text == "":
            return ''.join(
                (
                    EventHTMLFormater.indent(command.indent),
                    '<font color="red"><b>ERROR:</b> Event code [%s] defined but not implemented</font>' %
                    command.code
                )
            )
        return ''.join(
            (
                EventHTMLFormater.indent(command.indent),
                text
            )
        )

    @staticmethod
    def get_event_formater(code):
        name = "Command%03dFormater" % code
        return Kernel.System.load(name)


class EventHTMLFormater(object):

    @staticmethod
    def red(text):
        return '<font color="red">%s</font>' % text

    @staticmethod
    def blue(text):
        return '<font color="blue">%s</font>' % text

    @staticmethod
    def green(text):
        return '<font color="green">%s</font>' % text

    @staticmethod
    def bold(text):
        return '<b>%s</b>' % text

    @staticmethod
    def italic(text):
        return '<i>%s</i>' % text

    @staticmethod
    def color(color, text):
        return '<font color="%s">%s</font>' % (color, text)

    @staticmethod
    def colorObj(color):
        template = EventHTMLFormater.color('black', '<b>Color</b>(%s, %s, %s, %s)')
        colors = (
            EventHTMLFormater.red('%3d'),
            EventHTMLFormater.green('%3d'),
            EventHTMLFormater.blue('%3d'),
            EventHTMLFormater.bold('%3d')
        )
        data = (
            color.red,
            color.green,
            color.blue,
            color.alpha
        )
        return (template % colors) % data

    @staticmethod
    def audioFile(audiofile):
        template = EventHTMLFormater.color(
            'black', '<b>Audio</b>{:name => %s, :volume => %s, :pitch => %s}')
        colors = (
            EventHTMLFormater.green('%s'),
            EventHTMLFormater.red('%3d'),
            EventHTMLFormater.red('%3d')
        )
        data = (
            audiofile.name,
            audiofile.volume,
            audiofile.pitch
        )
        return (template % colors) % data

    @staticmethod
    def item(item):
        template = EventHTMLFormater.color('black', 'Item [%s: %s]')
        colors = (EventHTMLFormater.red('%03d'), EventHTMLFormater.green('%s'))
        data = (item.id, item.name)
        return (template % colors) % data

    @staticmethod
    def weapon(weapon):
        template = EventHTMLFormater.color('black', 'Weapon [%s: %s]')
        colors = (EventHTMLFormater.red('%03d'), EventHTMLFormater.green('%s'))
        data = (weapon.id, weapon.name)
        return (template % colors) % data

    @staticmethod
    def armor(armor):
        template = EventHTMLFormater.color('black', 'Armor [%s: %s]')
        colors = (EventHTMLFormater.red('%03d'), EventHTMLFormater.green('%s'))
        data = (armor.id, armor.name)
        return (template % colors) % data

    @staticmethod
    def indent(level):
        return "&nbsp;" * 4 * level


class Command000Formater(object):

    """place holder"""

    @staticmethod
    def formatCommand(params):
        f = {}
        f['params'] = params
        return Command000Formater.template(f)

    @staticmethod
    def template(f):
        return EventHTMLFormater.color('#0000A0', EventHTMLFormater.bold('@>'))


class Command101Formater(object):

    """Show Text"""

    @staticmethod
    def formatCommand(params):
        f = {}
        f['text'] = params[0]
        return Command101Formater.template(f)

    @staticmethod
    def template(f):
        template = '%s %s' % (
            EventHTMLFormater.green('Text:'), EventHTMLFormater.italic('%(text)s'))
        return template % f


class Command401Formater(object):

    """Show Text Extra Lines"""

    @staticmethod
    def formatCommand(params):
        f = {}
        f['text'] = params[0]
        return Command401Formater.template(f)

    @staticmethod
    def template(f):
        template = '&nbsp;&nbsp;&nbsp;&nbsp;%s %s' % (
            EventHTMLFormater.green(':'), EventHTMLFormater.italic('%(text)s'))
        return template % f


class Command102Formater(object):

    """Show Choices"""

    @staticmethod
    def formatCommand(params):
        f = {}
        f['choice_number'] = len(params[0])
        f['choice_choices'] = params[0]
        f['choice_default'] = params[1]
        return Command102Formater.template(f)

    @staticmethod
    def template(f):
        choices = ''
        for i in range(f['choice_number']):
            choices += '(%s)%s' % (EventHTMLFormater.red(i),
                                   EventHTMLFormater.green(f['choice_choices'][i]))
            if i < f['choice_number'] - 1:
                choices += ', '
        f['choice_text'] = choices
        template = ('%s ' * 5) % (
            EventHTMLFormater.color('#25383C', 'Show Choices:'),
            EventHTMLFormater.blue(EventHTMLFormater.bold(' Case')),
            EventHTMLFormater.italic('[%(choice_text)s]'),
            EventHTMLFormater.blue(EventHTMLFormater.bold('Default')),
            EventHTMLFormater.red('%(choice_default)d')
        )
        return template % f


class Command402Formater(object):

    """When [**] The command that serves as an entry point for each potential choice"""

    @staticmethod
    def formatCommand(params):
        f = {}
        f['choice_name'] = params[1]
        f['choice_id'] = params[0]
        return Command402Formater.template(f)

    @staticmethod
    def template(f):
        template = '&nbsp;&nbsp;%s (%s)%s' % (EventHTMLFormater.blue(EventHTMLFormater.bold(
            'When')), EventHTMLFormater.red('%(choice_id)s'), EventHTMLFormater.green('%(choice_name)s'))
        return template % f


class Command403Formater(object):

    """When Cancel Choices"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command403Formater.template(f)

    @staticmethod
    def template(f):
        return '&nbsp;&nbsp;%s %s' % (EventHTMLFormater.blue(EventHTMLFormater.bold('When')), EventHTMLFormater.green('Cancel'))


class Command103Formater(object):

    """Input Number"""

    @staticmethod
    def formatCommand(params):
        project = Kernel.GlobalObjects["PROJECT"]
        system = project.getData('System')
        f = {}
        f['variable_id'] = params[0]
        f['variable_name'] = system.variables[params[0]]
        f['digits'] = params[1]
        return Command103Formater.template(f)

    @staticmethod
    def template(f):
        template = '%s Variable[%s: %s], (%s digit(s))' % (EventHTMLFormater.blue('Input Number:'),
                                                           EventHTMLFormater.red(
                                                               '%(variable_id)04d'),
                                                           EventHTMLFormater.green(
                                                               '%(variable_name)s'),
                                                           EventHTMLFormater.bold('%(digits)s'))
        return template % f


class Command104Formater(object):

    """Change Text Options"""

    @staticmethod
    def formatCommand(params):
        f = {}
        pos_dict = {
            0: 'Top',  1: 'Middle', 2: 'Bottom'
        }
        visible_dict = {
            0: 'Show',  1: 'Hide'
        }
        f['msg_pos'] = pos_dict[params[0]]
        f['msg_frame'] = visible_dict[params[1]]
        return Command104Formater.template(f)

    @staticmethod
    def template(f):
        template = '%s [%s, %s]' % (EventHTMLFormater.italic('Change Text Options:'), EventHTMLFormater.bold(
            '%(msg_pos)s'), EventHTMLFormater.bold('%(msg_frame)s'))
        return template % f


class Command105Formater(object):

    """Button Input Processing"""

    @staticmethod
    def formatCommand(params):
        project = Kernel.GlobalObjects["PROJECT"]
        system = project.getData('System')

        f = {}
        f['var_id'] = params[0]
        f['var_name'] = system.variables[params[0]]
        return Command105Formater.template(f)

    @staticmethod
    def template(f):
        template = '%s Variable[%s: %s]' % (EventHTMLFormater.bold(EventHTMLFormater.red(
            'Button Input Processing: ')), EventHTMLFormater.red('%(var_id)04d'), EventHTMLFormater.green('%(var_name)s'))
        return template % f


class Command106Formater(object):

    """Wait"""

    @staticmethod
    def formatCommand(params):
        f = {}
        f['frames'] = params[0]
        return Command106Formater.template(f)

    @staticmethod
    def template(f):
        template = '%s %s %s' % (EventHTMLFormater.blue(EventHTMLFormater.bold(
            'Wait:')), EventHTMLFormater.red('%(frames)s'), EventHTMLFormater.red('Frame(s)'))
        return template % f


class Command108Formater(object):

    """Comment"""

    @staticmethod
    def formatCommand(params):
        f = {}
        f['text'] = params[0]
        return Command108Formater.template(f)

    @staticmethod
    def template(f):
        template = '%s %s' % (EventHTMLFormater.green(
            'Comment:'), EventHTMLFormater.italic(EventHTMLFormater.green('%(text)s')))
        return template % f


class Command408Formater(object):

    """Comment Extra Lines"""

    @staticmethod
    def formatCommand(params):
        f = {}
        f['text'] = params[0]
        return Command408Formater.template(f)

    @staticmethod
    def template(f):
        template = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%s %s' % (
            EventHTMLFormater.green(':'), EventHTMLFormater.italic(EventHTMLFormater.green('%(text)s')))
        return template % f


class Command111Formater(object):

    """Conditional Branch"""

    @staticmethod
    def formatCommand(params):
        f = {}
        mode = params[0]
        mode_dict = {
            0: 'Switch',  1: 'Variable', 2: 'Self Switch', 3: 'Timer',
            4: 'Actor', 5: 'Enemy', 6: 'character', 7: 'Gold', 8: 'Item',
            9: 'Weapon', 10: 'Armor', 11: 'Button', 12: 'Script'
        }
        f['mode'] = mode
        f['mode_name'] = mode_dict[params[0]]

        project = Kernel.GlobalObjects["PROJECT"]
        system = project.getData('System')

        if mode == 0:  # switch
            f['switch_id'] = params[1]
            f['switch_name'] = system.switches[params[1]]
            if params[2] == 0:
                f['switch_state'] = 'True'
            else:
                f['switch_state'] = 'False'
        elif mode == 1:  # variable
            f['var_one_id'] = params[1]
            f['var_one_name'] = system.variables[params[1]]
            f['var_two_mode'] = params[2]
            if params[2] == 0:
                f['var_two_value'] = params[3]
            else:
                f['var_two_id'] = params[3]
                f['var_two_name'] = system.variables[params[3]]
            operation_dict = {
                0: '==', 1: '>=', 2: '<=', 3: '>', 4: '<', 5: '!='}
            f['operation'] = operation_dict[params[4]]
        elif mode == 2:  # self switch
            f['self_switch'] = params[1]
            if params[2] == 0:
                f['switch_state'] = 'True'
            else:
                f['switch_state'] = 'False'
        elif mode == 3:  # timer
            f['time'] = params[1]
            f['time_mode'] = params[2]
        elif mode == 4:  # actor
            actors = project.getData('Actors')
            f['actor_id'] = params[1]
            f['actor_name'] = actors[params[1]].name
            f['actor_mode'] = params[2]
            if params[2] == 1:  # name
                f['actor_condition_name'] = params[3]
            elif params[2] == 2:  # skill
                skills = project.getData('Skills')
                f['skill_id'] = params[3]
                f['skill_name'] = skills[params[3]].name
            elif params[2] == 3:  # weapon
                weapons = project.getData('Weapons')
                f['weapon_id'] = params[3]
                f['weapon_name'] = weapons[params[3]].name
            elif params[2] == 4:  # armor
                armors = project.getData('Armors')
                f['armor_id'] = params[3]
                f['armor_name'] = armors[params[3]].name
            elif params[2] == 5:  # state
                states = project.getData('States')  # system.states
                f['state_id'] = params[3]
                f['state_name'] = states[params[3]].name
            if params[2] != 0:
                f['actor_condition'] = params[3]
        elif mode == 5:  # enemy
            f['enemy_position'] = params[1]
            f['enemy_mode'] = params[2]
            f['enemy_state_id'] = params[3]
            f['enemy_state_name'] = system.states[params[3]]
        elif mode == 6:  # character
            f['character_id'] = params[1]
            f['character_direction'] = params[2]
        elif mode == 7:  # gold
            f['gold_mode'] = params[2]
            f['gold_value'] = params[1]
        elif mode == 8:  # item
            items = project.getData('Items')
            f['item_id'] = params[1]
            f['item_name'] = items[params[1]].name
        elif mode == 9:  # weapon
            weapons = project.getData('Weapons')
            f['weapon_id'] = params[1]
            f['weapon_name'] = weapons[params[1]].name
        elif mode == 10:  # armor
            armors = project.getData('Armors')
            f['armor_id'] = params[1]
            f['armor_name'] = armors[params[1]].name
        elif mode == 11:  # button
            f['button'] = params[1]
        elif mode == 12:
            f['script'] = params[1]
        else:
            pass

        return Command111Formater.template(f)

    @staticmethod
    def template(f):
        mode = f['mode']
        template = (EventHTMLFormater.blue('Conditional Branch: %s') %
                    EventHTMLFormater.bold('if')) + ' %s'
        html = (EventHTMLFormater.red('%s Missing handeler for mode [%s]') % (
            EventHTMLFormater.bold('ERROR[Code 111: Conditional Branch]:'), '%(mode)s')) % f
        if mode == 0:  # switch
            html = (EventHTMLFormater.color('black', 'Switch [%s: %s] %s %s') % (
                EventHTMLFormater.red('%(switch_id)04d'),
                EventHTMLFormater.green('%(switch_name)s'),
                EventHTMLFormater.bold('=='),
                EventHTMLFormater.blue(EventHTMLFormater.bold('%(switch_state)s'))
            )) % f
        elif mode == 1:  # variable
            if f['var_two_mode'] == 0:
                html = ('Variable [%s: %s] %s %s' % (
                    EventHTMLFormater.red('%(var_one_id)04d'),
                    EventHTMLFormater.green('%(var_one_name)s'),
                    EventHTMLFormater.bold('%(operation)s'),
                    EventHTMLFormater.bold('%(var_two_value)s')
                )) % f
            else:
                html = ('Variable [%s: %s] %s Variable [%s: %s]' % (
                    EventHTMLFormater.red('%(var_one_id)04d'),
                    EventHTMLFormater.green('%(var_one_name)s'),
                    EventHTMLFormater.bold('%(operation)s'),
                    EventHTMLFormater.red('%(var_two_id)04d'),
                    EventHTMLFormater.green('%(var_two_name)s')
                )) % f
        elif mode == 2:  # self switch
            html = ('Self Switch %s %s %s' % (
                EventHTMLFormater.green('%(self_switch)s'),
                EventHTMLFormater.bold('=='),
                EventHTMLFormater.green('%(switch_state)s')
            )) % f
        elif mode == 3:  # timer
            if f['time_mode'] == 0:
                html = ('Timer %s %s seconds' % (
                    EventHTMLFormater.bold('>='), EventHTMLFormater.red('%(time)s'))) % f
            else:
                html = ('Timer %s %s seconds' % (
                    EventHTMLFormater.bold("<="), EventHTMLFormater.red('%(time)s'))) % f
        elif mode == 4:  # actor
            if f['actor_mode'] == 0:  # in party
                html = ('Actor [%s: %s] %s in party' % (
                    EventHTMLFormater.red('%(actor_id)s'),
                    EventHTMLFormater.green('%(actor_name)s'),
                    EventHTMLFormater.bold('is')
                )) % f
            elif f['actor_mode'] == 1:  # name
                html = ('Actor [%s: %s] %s %s' % (
                    EventHTMLFormater.red('%(actor_id)s'),
                    EventHTMLFormater.green('%(actor_name)s'),
                    EventHTMLFormater.bold('=='),
                    EventHTMLFormater.green('%(actor_condition_name)s')
                )) % f
            elif f['actor_mode'] == 2:  # skill
                html = ('Actor [%s: %s] Has Skill [%s: %s]' % (
                    EventHTMLFormater.red('%(actor_id)s'),
                    EventHTMLFormater.green('%(actor_name)s'),
                    EventHTMLFormater.red('%(skill_id)04d'),
                    EventHTMLFormater.green('%(skill_name)s')
                )) % f
            elif f['actor_mode'] == 3:  # weapon
                html = ('Actor [%s: %s] Has Weapon Equiped [%s: %s]' % (
                    EventHTMLFormater.red('%(actor_id)s'),
                    EventHTMLFormater.green('%(actor_name)s'),
                    EventHTMLFormater.red('%(weapon_id)04d'),
                    EventHTMLFormater.green('%(weapon_name)s')
                )) % f
            elif f['actor_mode'] == 4:  # armor
                html = ('Actor [%s: %s] Has Armor Equiped [%s: %s]' % (
                    EventHTMLFormater.red('%(actor_id)s'),
                    EventHTMLFormater.green('%(actor_name)s'),
                    EventHTMLFormater.red('%(armor_id)04d'),
                    EventHTMLFormater.green('%(armor_name)s')
                )) % f
            elif f['actor_mode'] == 5:  # state
                html = ('Actor [%s: %s] Has State [%s: %s]' % (
                    EventHTMLFormater.red('%(actor_id)s'),
                    EventHTMLFormater.green('%(actor_name)s'),
                    EventHTMLFormater.red('%(state_id)04d'),
                    EventHTMLFormater.green('%(state_name)s')
                )) % f
        elif mode == 5:  # enemy
            if f['enemy_mode'] == 0:  # appear
                html = ('Enemy at positon [%s] Appears' % EventHTMLFormater.red(
                    '%(enemy_position)s')) % f
            elif f['enemy_mode'] == 1:  # state
                html = ('Enemy at positon [%s] Has State [%s: %s]' % (
                    EventHTMLFormater.red('%(enemy_position)s'),
                    EventHTMLFormater.red('%(enemy_state_id)04d'),
                    EventHTMLFormater.green('%(enemy_state_name)s')
                )) % f
        elif mode == 6:  # character
            directionmap = {
                2: 'DOWN',
                4: 'LEFT',
                6: 'RIGHT',
                8: 'UP'
            }
            f['character_direction_name'] = directionmap[
                f['character_direction']]
            if f['character_id'] == -1:
                html = ('Player %s Facing %s' % (EventHTMLFormater.bold(
                    'is'), EventHTMLFormater.green('%(character_direction_name)s'))) % f
            elif f['character_id'] == 0:
                html = ('This Event %s Facing %s' % (EventHTMLFormater.bold(
                    'is'), EventHTMLFormater.green('%(character_direction_name)s'))) % f
            else:
                html = ('Event ID [%s] <b>is</b> Facing %(character_direction_name)s' % (
                    EventHTMLFormater.red('%(character_id)04d'),
                    EventHTMLFormater.bold('is'),
                    EventHTMLFormater.green('%(character_direction_name)s')
                )) % f
        elif mode == 7:  # gold
            if f['gold_mode'] == 0:
                html = ('Party Gold %s %s' % (
                    EventHTMLFormater.bold('>='), EventHTMLFormater.red('%(gold_value)s'))) % f
            else:
                html = ('Party Gold %s %s' % (
                    EventHTMLFormater.bold('<='), EventHTMLFormater.red('%(gold_value)s'))) % f
        elif mode == 8:  # item
            html = ('Party Has At Least One of Item [%s: %s]' % (
                EventHTMLFormater.red('%(item_id)04d'), EventHTMLFormater.green('%(item_name)s'))) % f
        elif mode == 9:  # weapon
            html = ('Party Has At Least One of Weapon [%s: %s]' % (
                EventHTMLFormater.red('%(weapon_id)04d'), EventHTMLFormater.green('%(weapon_name)s'))) % f
        elif mode == 10:  # armor
            html = ('Party Has At Least One of Armor [%s: %s]' % (
                EventHTMLFormater.red('%(armor_id)04d'), EventHTMLFormater.green('%(armor_name)s'))) % f
        elif mode == 11:  # button
            buttonmap = {
                2: 'DOWN',
                4: 'LEFT',
                6: 'RIGHT',
                8: 'UP',
                11: 'A',
                12: 'B',
                13: 'C',
                14: 'X',
                15: 'Y',
                16: 'Z',
                17: 'L',
                18: 'R',
                21: 'SHIFT',
                22: 'CTRL',
                23: 'ALT',
                25: 'F5',
                26: 'F6',
                27: 'F7',
                28: 'F8',
                29: 'F9',
            }
            f['button_name'] = buttonmap[f['button']]
            html = ('Button [%s] %s Pressed' % (
                EventHTMLFormater.red('%(button_name)s'), EventHTMLFormater.bold('is'))) % f
        else:  # script
            html = 'Script: '
            lines = f['script'].split('\n')
            html += EventHTMLFormater.italic(Kernel.escapeHTML(lines[0]))

        body = template % html
        return body


class Command411Formater(object):

    """Else"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command411Formater.template(f)

    @staticmethod
    def template(f):
        return '%s' % (EventHTMLFormater.blue('Else'))


class Command112Formater(object):

    """Loop"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command112Formater.template(f)

    @staticmethod
    def template(f):
        return '%s' % (EventHTMLFormater.blue('Loop'))


class Command413Formater(object):

    """Repeat Above"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command413Formater.template(f)

    @staticmethod
    def template(f):
        return '%s' % (EventHTMLFormater.blue('Repeat Above'))


class Command113Formater(object):

    """Break Loop"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command113Formater.template(f)

    @staticmethod
    def template(f):
        return '%s' % (EventHTMLFormater.blue('Break Loop'))


class Command115Formater(object):

    """Exit Event Processing"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command115Formater.template(f)

    @staticmethod
    def template(f):
        return '%s' % (EventHTMLFormater.red(EventHTMLFormater.bold('Exit Event Processing')))


class Command116Formater(object):

    """Erase Event"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command116Formater.template(f)

    @staticmethod
    def template(f):
        return '%s' % (EventHTMLFormater.red(EventHTMLFormater.bold('Erase Event')))


class Command117Formater(object):

    """Call Common Event"""

    @staticmethod
    def formatCommand(params):
        f = {}
        f['commonevent_id'] = params[0]
        return Command117Formater.template(f)

    @staticmethod
    def template(f):
        template = '%s: ID [%s]' % (EventHTMLFormater.red(
            'Call Common Event'), EventHTMLFormater.red(EventHTMLFormater.bold('%(commonevent_id)s')))
        return template % f


class Command118Formater(object):

    """Label"""

    @staticmethod
    def formatCommand(params):
        f = {}
        f['label_name'] = params[0]
        return Command118Formater.template(f)

    @staticmethod
    def template(f):
        template = '%s: %s' % (
            EventHTMLFormater.blue('Label'), EventHTMLFormater.green('%(label_name)s'))
        return template % f


class Command119Formater(object):

    """Jump to Label"""

    @staticmethod
    def formatCommand(params):
        f = {}
        f['jump_to_name'] = params[0]
        return Command119Formater.template(f)

    @staticmethod
    def template(f):
        template = '%s: %s' % (EventHTMLFormater.blue('Jump to Label'), EventHTMLFormater.green(
            EventHTMLFormater.italic('%(jump_to_name)s')))
        return template % f


class Command121Formater(object):

    """Control Switches"""

    @staticmethod
    def formatCommand(params):
        f = {}
        project = Kernel.GlobalObjects["PROJECT"]
        system = project.getData('System')
        f['params'] = params
        f['switch_1_id'] = params[0]
        f['switch_1_name'] = system.switches[params[0]]
        f['switch_2_id'] = params[1]
        f['switch_2_name'] = system.switches[params[1]]
        if params[2] == 0:
            f['switch_state'] = 'True'
        else:
            f['switch_state'] = 'False'
        return Command121Formater.template(f)

    @staticmethod
    def template(f):
        if f['switch_2_id'] == f['switch_1_id']:  # only modifying 1 var
            template = '%s Switch [%s: %s] = %s' % (
                EventHTMLFormater.red('Control Switch:'),
                EventHTMLFormater.red('%(switch_1_id)s'),
                EventHTMLFormater.green('%(switch_1_name)s'),
                EventHTMLFormater.blue(EventHTMLFormater.bold('%(switch_state)s'))
            )
        else:
            template = '%s [%s: %s] -> [%s:%s] = %s' % (
                EventHTMLFormater.red('Control Switchs:'),
                EventHTMLFormater.red('%(switch_1_id)s'),
                EventHTMLFormater.green('%(switch_1_name)s'),
                EventHTMLFormater.red('%(switch_2_id)s'),
                EventHTMLFormater.green('%(switch_2_name)s'),
                EventHTMLFormater.blue(EventHTMLFormater.bold('%(switch_state)s'))
            )
        return template % f


class Command122Formater(object):

    """Control Variables"""

    @staticmethod
    def formatCommand(params):
        f = {}
        f['batch_low'] = params[0]
        f['batch_high'] = params[1]

        operator_dict = {
            0: '= ', 1: '+= ', 2: '-= ', 3: '*= ', 4: '/= ', 5: '%= '
        }
        f['operation'] = operator_dict[params[2]]
        f['operand'] = params[3]

        if(params[4] & 0x80000000):
            f['op_param1'] = -0x100000000 + params[4]
        else:
            f['op_param1'] = params[4]

        if params[3] == 2 or params[3] == 4 or params[3] == 5 or params[3] == 6:
            if(params[5] & 0x80000000):
                f['op_param2'] = -0x100000000 + params[5]
            else:
                f['op_param2'] = params[5]

        return Command122Formater.template(f)

    @staticmethod
    def template(f):
        template = '%s: ' % (EventHTMLFormater.red('Control Variables'))
        project = Kernel.GlobalObjects["PROJECT"]
        system = project.getData('System')
        # Draw variable or batch
        if f['batch_low'] == f['batch_high']:
            f['var_name'] = system.variables[f['batch_low']]
            template += '[%s: %s] ' % (
                EventHTMLFormater.bold('%(batch_low)04d'), EventHTMLFormater.red('%(var_name)s'))
        else:
            template += '[%s..%s] ' % (
                EventHTMLFormater.red('%(batch_low)04d'), EventHTMLFormater.red('%(batch_high)04d'))
        # Draw operation symbol
        template += '%s' % (EventHTMLFormater.red('%(operation)s'))
        # Draw operand
        if f['operand'] == 0:  # constant
            template += '%s' % (
                EventHTMLFormater.red(EventHTMLFormater.italic('%(op_param1)s')))
        elif f['operand'] == 1:  # variable
            f['opr_var_name'] = system.variables[f['op_param1']]
            template += '[%s: %s] ' % (
                EventHTMLFormater.bold('%(op_param1)04d'), EventHTMLFormater.red('%(opr_var_name)s'))
        elif f['operand'] == 2:  # random number
            template += '%s(%s, %s)' % (EventHTMLFormater.bold('rand'),
                                        EventHTMLFormater.red('%(op_param1)s'), EventHTMLFormater.red('%(op_param2)s'))
        elif f['operand'] == 3:  # item
            items = project.getData('Items')
            f['item_name'] = items[f['op_param1']].name
            template += '[%s: %s] In Inventory' % (
                EventHTMLFormater.red('%(op_param1)04d'), EventHTMLFormater.red('%(item_name)s'))
        elif f['operand'] == 4:  # actor
            actors = project.getData('Actors')
            f['actor_name'] = actors[f['op_param1']].name
            template += '[%s: %s].' % (
                EventHTMLFormater.red('%(op_param1)04d'), EventHTMLFormater.red('%(actor_name)s'))
            if f['op_param2'] == 0:  # Level
                template += '%s' % (EventHTMLFormater.bold('level'))
            elif f['op_param2'] == 1:  # EXP
                template += '%s' % (EventHTMLFormater.bold('exp'))
            elif f['op_param2'] == 2:  # HP
                template += '%s' % (EventHTMLFormater.bold('hp'))
            elif f['op_param2'] == 3:  # SP
                template += '%s' % (EventHTMLFormater.bold('sp'))
            elif f['op_param2'] == 4:  # MaxHP
                template += '%s' % (EventHTMLFormater.bold('maxhp'))
            elif f['op_param2'] == 5:  # MaxSP
                template += '%s' % (EventHTMLFormater.bold('maxsp'))
            elif f['op_param2'] == 6:  # STR
                template += '%s' % (EventHTMLFormater.bold('str'))
            elif f['op_param2'] == 7:  # DEX
                template += '%s' % (EventHTMLFormater.bold('dex'))
            elif f['op_param2'] == 8:  # AGI
                template += '%s' % (EventHTMLFormater.bold('agi'))
            elif f['op_param2'] == 9:  # INT
                template += '%s' % (EventHTMLFormater.bold('int'))
            elif f['op_param2'] == 10:  # ATK
                template += '%s' % (EventHTMLFormater.bold('atk'))
            elif f['op_param2'] == 11:  # PDEF
                template += '%s' % (EventHTMLFormater.bold('pdef'))
            elif f['op_param2'] == 12:  # MDEF
                template += '%s' % (EventHTMLFormater.bold('mdef'))
            elif f['op_param2'] == 13:  # EVA
                template += '%s' % (EventHTMLFormater.bold('eva'))
        elif f['operand'] == 5:  # enemy
            template += 'Enemy at positon [%s].' % (
                EventHTMLFormater.red('%(op_param1)s'))
            if f['op_param2'] == 0:
                template += '%s' % (EventHTMLFormater.bold('hp'))
            elif f['op_param2'] == 1:  # SP
                template += '%s' % (EventHTMLFormater.bold('sp'))
            elif f['op_param2'] == 2:  # MaxHP
                template += '%s' % (EventHTMLFormater.bold('maxhp'))
            elif f['op_param2'] == 3:  # MaxSP
                template += '%s' % (EventHTMLFormater.bold('maxsp'))
            elif f['op_param2'] == 4:  # STR
                template += '%s' % (EventHTMLFormater.bold('str'))
            elif f['op_param2'] == 5:  # DEX
                template += '%s' % (EventHTMLFormater.bold('dex'))
            elif f['op_param2'] == 6:  # AGI
                template += '%s' % (EventHTMLFormater.bold('agi'))
            elif f['op_param2'] == 7:  # INT
                template += '%s' % (EventHTMLFormater.bold('int'))
            elif f['op_param2'] == 8:  # PDEF
                template += '%s' % (EventHTMLFormater.bold('pdef'))
            elif f['op_param2'] == 9:  # MDEF
                template += '%s' % (EventHTMLFormater.bold('mdef'))
            elif f['op_param2'] == 10:  # EVA
                template += '%s' % (EventHTMLFormater.bold('eva'))
        elif f['operand'] == 6:  # character
            if f['op_param1'] == -1:  # player
                template += '[Player].'
            elif f['op_param1'] == 0:  # this event
                template += '[This Event].'
            else:
                template += 'Event[%s].' % (
                    EventHTMLFormater.red('%(op_param1)04d'))
            # Choice
            if f['op_param2'] == 0:  # Map X
                template += '%s' % (EventHTMLFormater.bold('map_x'))
            elif f['op_param2'] == 1:  # Map Y
                template += '%s' % (EventHTMLFormater.bold('map_y'))
            elif f['op_param2'] == 2:  # Direction
                template += '%s' % (EventHTMLFormater.bold('direction'))
            elif f['op_param2'] == 3:  # Screen X
                template += '%s' % (EventHTMLFormater.bold('screen_x'))
            elif f['op_param2'] == 4:  # Screen Y
                template += '%s' % (EventHTMLFormater.bold('screen_y'))
            elif f['op_param2'] == 5:  # Terrain Tag
                template += '%s' % (EventHTMLFormater.bold('terrain_tag'))
        elif f['operand'] == 7:  # other
            if f['op_param1'] == 0:  # Map ID
                template += '%s' % (EventHTMLFormater.bold('Map ID'))
            elif f['op_param1'] == 1:  # Party Members
                template += '%s' % (EventHTMLFormater.bold('Party Members'))
            elif f['op_param1'] == 2:  # Gold
                template += '%s' % (EventHTMLFormater.bold('Gold'))
            elif f['op_param1'] == 3:  # Steps
                template += '%s' % (EventHTMLFormater.bold('Steps'))
            elif f['op_param1'] == 4:  # Play Time
                template += '%s' % (EventHTMLFormater.bold('Play Time'))
            elif f['op_param1'] == 5:  # Timer
                template += '%s' % (EventHTMLFormater.bold('Timer'))
            elif f['op_param1'] == 6:  # Save Count
                template += '%s' % (EventHTMLFormater.bold('Save Count'))

        return template % f


class Command123Formater(object):

    """Control Self Switch"""

    @staticmethod
    def formatCommand(params):
        f = {}
        f['self_switch'] = params[0]
        if params[1] == 0:
            f['switch_state'] = 'True'
        else:
            f['switch_state'] = 'False'
        return Command123Formater.template(f)

    @staticmethod
    def template(f):
        template = '%s: %s %s %s' % (EventHTMLFormater.red('Control Self Switch'),
                                     EventHTMLFormater.green('%(self_switch)s'),
                                     EventHTMLFormater.bold('='),
                                     EventHTMLFormater.green('%(switch_state)s'))
        return template % f


class Command124Formater(object):

    """Control Timer"""

    @staticmethod
    def formatCommand(params):
        f = {}
        f['timer_state'] = params[0]
        if params[0] == 0:
            f['timer_countdown'] = params[1]
        return Command124Formater.template(f)

    @staticmethod
    def template(f):
        if f['timer_state'] == 0:
            template = '%s: %s (%s seconds)' % (EventHTMLFormater.bold('Control Timer'),
                                                EventHTMLFormater.red(
                                                    EventHTMLFormater.italic('Start')),
                                                EventHTMLFormater.red('%(timer_countdown)s'))
        else:
            template = '%s: %s' % (EventHTMLFormater.bold(
                'Control Timer'), EventHTMLFormater.red(EventHTMLFormater.italic('Stop')))
        return template % f


class Command125Formater(object):

    """Change Gold"""

    @staticmethod
    def formatCommand(params):
        f = {}
        operation = {0: '+', 1: '-'}
        f['operation'] = operation[params[0]]
        f['operand_type'] = params[1]
        f['operand'] = params[2]
        return Command125Formater.template(f)

    @staticmethod
    def template(f):
        template = '%s: %s' % (EventHTMLFormater.italic(
            EventHTMLFormater.green('Change Gold')), EventHTMLFormater.bold('%(operation)s'))
        if f['operand_type'] == 0:  # constant
            template += '%s' % (
                EventHTMLFormater.bold(EventHTMLFormater.red('%(operand)s')))
        else:                           # variable
            project = Kernel.GlobalObjects["PROJECT"]
            system = project.getData('System')
            f['var_name'] = system.variables[f['operand']]
            template += 'Variable [%s: %s]' % (
                EventHTMLFormater.bold('%(operand)04d'), EventHTMLFormater.red('%(var_name)s'))
        return template % f


class Command126Formater(object):

    """Change Items"""

    @staticmethod
    def formatCommand(params):
        f = {}
        f['item_id'] = params[0]
        operation = {0: '+', 1: '-'}
        f['operation'] = operation[params[1]]
        f['operand_type'] = params[2]
        f['operand'] = params[3]
        return Command126Formater.template(f)

    @staticmethod
    def template(f):
        project = Kernel.GlobalObjects["PROJECT"]
        items = project.getData('Items')
        f['item_name'] = items[f['item_id']].name
        template = '%s: [%s: %s], %s' % (EventHTMLFormater.italic(EventHTMLFormater.green('Change Items')), EventHTMLFormater.blue('%(item_id)04d'),
                                         EventHTMLFormater.blue('%(item_name)s'), EventHTMLFormater.bold('%(operation)s'))
        if f['operand_type'] == 0:  # constant
            template += '%s' % (
                EventHTMLFormater.bold(EventHTMLFormater.red('%(operand)s')))
        else:                           # variable
            system = project.getData('System')
            f['var_name'] = system.variables[f['operand']]
            template += 'Variable [%s: %s]' % (
                EventHTMLFormater.bold('%(operand)04d'), EventHTMLFormater.red('%(var_name)s'))
        return template % f


class Command127Formater(object):

    """Change Weapons"""

    @staticmethod
    def formatCommand(params):
        f = {}
        f['weapon_id'] = params[0]
        operation = {0: '+', 1: '-'}
        f['operation'] = operation[params[1]]
        f['operand_type'] = params[2]
        f['operand'] = params[3]
        return Command127Formater.template(f)

    @staticmethod
    def template(f):
        project = Kernel.GlobalObjects["PROJECT"]
        weapons = project.getData('Weapons')
        f['weapon_name'] = weapons[f['weapon_id']].name
        template = '%s: [%s: %s], %s' % (EventHTMLFormater.italic(EventHTMLFormater.green('Change Weapons')), EventHTMLFormater.blue('%(weapon_id)04d'),
                                         EventHTMLFormater.blue('%(weapon_name)s'), EventHTMLFormater.bold('%(operation)s'))
        if f['operand_type'] == 0:  # constant
            template += '%s' % (
                EventHTMLFormater.bold(EventHTMLFormater.red('%(operand)s')))
        else:                           # variable
            system = project.getData('System')
            f['var_name'] = system.variables[f['operand']]
            template += 'Variable [%s: %s]' % (
                EventHTMLFormater.bold('%(operand)04d'), EventHTMLFormater.red('%(var_name)s'))
        return template % f


class Command128Formater(object):

    """Change Armor"""

    @staticmethod
    def formatCommand(params):
        f = {}
        f['armor_id'] = params[0]
        operation = {0: '+', 1: '-'}
        f['operation'] = operation[params[1]]
        f['operand_type'] = params[2]
        f['operand'] = params[3]
        return Command128Formater.template(f)

    @staticmethod
    def template(f):
        project = Kernel.GlobalObjects["PROJECT"]
        armors = project.getData('Armors')
        f['armor_name'] = armors[f['armor_id']].name
        template = '%s: [%s: %s], %s' % (EventHTMLFormater.italic(EventHTMLFormater.green('Change Armors')), EventHTMLFormater.blue('%(armor_id)04d'),
                                         EventHTMLFormater.blue('%(armor_name)s'), EventHTMLFormater.bold('%(operation)s'))
        if f['operand_type'] == 0:  # constant
            template += '%s' % (
                EventHTMLFormater.bold(EventHTMLFormater.red('%(operand)s')))
        else:                           # variable
            system = project.getData('System')
            f['var_name'] = system.variables[f['operand']]
            template += 'Variable [%s: %s]' % (
                EventHTMLFormater.bold('%(operand)04d'), EventHTMLFormater.red('%(var_name)s'))
        return template % f


class Command129Formater(object):

    """Change Party Member"""

    @staticmethod
    def formatCommand(params):
        f = {}
        f['actor_id'] = params[0]
        project = Kernel.GlobalObjects["PROJECT"]
        actors = project.getData('Actors')
        f['actor_name'] = actors[params[0]].name
        operation = {0: 'Add', 1: 'Remove'}
        f['operation'] = operation[params[1]]
        f['initialize'] = params[2]
        return Command129Formater.template(f)

    @staticmethod
    def template(f):
        template = '%s: %s Actor[%s: %s]' % (EventHTMLFormater.blue('Change Party Member'), EventHTMLFormater.red('%(operation)s'),
                                             EventHTMLFormater.red('%(actor_id)04d'), EventHTMLFormater.red('%(actor_name)s'))
        if f['initialize'] == 1:  # Initialize Actor
            template += ', Initialize'
        return template % f


class Command131Formater(object):

    """Change Windowskin"""

    @staticmethod
    def formatCommand(params):
        f = {}
        f['winskin_name'] = params[0]
        return Command131Formater.template(f)

    @staticmethod
    def template(f):
        template = '%s: %s' % (EventHTMLFormater.bold(
            'Change Windowskin'), EventHTMLFormater.green('%(winskin_name)s'))
        return template % f


class Command132Formater(object):

    """Change Battle BGM"""

    @staticmethod
    def formatCommand(params):
        f = {}
        f['params'] = params
        f['se_file'] = params[0]
        return Command132Formater.template(f)

    @staticmethod
    def template(f):
        template = '%s %s' % (
            EventHTMLFormater.color('#348781', 'Change Battle BGM:'),
            EventHTMLFormater.audioFile(f['se_file'])
        )
        return template % f


class Command133Formater(object):

    """Change Battle End ME"""

    @staticmethod
    def formatCommand(params):
        f = {}
        f['params'] = params
        f['se_file'] = params[0]
        return Command133Formater.template(f)

    @staticmethod
    def template(f):
        template = '%s %s' % (
            EventHTMLFormater.color('#348781', 'Change Battle End ME:'),
            EventHTMLFormater.audioFile(f['se_file'])
        )
        return template % f


class Command134Formater(object):

    """Change Save Access"""

    @staticmethod
    def formatCommand(params):
        f = {}
        f['can_save'] = params[0]
        return Command134Formater.template(f)

    @staticmethod
    def template(f):
        if f['can_save'] == 0:
            return '%s: %s' % (EventHTMLFormater.bold(EventHTMLFormater.blue('Change Save Access')), EventHTMLFormater.red('Disabled'))
        else:
            return '%s: %s' % (EventHTMLFormater.bold(EventHTMLFormater.blue('Change Save Access')), EventHTMLFormater.green('Enabled'))


class Command135Formater(object):

    """Change Menu Access"""

    @staticmethod
    def formatCommand(params):
        f = {}
        f['access_menu'] = params[0]
        return Command135Formater.template(f)

    @staticmethod
    def template(f):
        if f['access_menu'] == 0:
            return '%s: %s' % (EventHTMLFormater.bold(EventHTMLFormater.blue('Change Menu Access')), EventHTMLFormater.red('Disabled'))
        else:
            return '%s: %s' % (EventHTMLFormater.bold(EventHTMLFormater.blue('Change Menu Access')), EventHTMLFormater.green('Enabled'))


class Command136Formater(object):

    """Change Encounter"""

    @staticmethod
    def formatCommand(params):
        f = {}
        f['can_encounter'] = params[0]
        return Command136Formater.template(f)

    @staticmethod
    def template(f):
        if f['can_encounter'] == 0:
            return '%s: %s' % (EventHTMLFormater.bold(EventHTMLFormater.blue('Change Encounter')), EventHTMLFormater.red('Disabled'))
        else:
            return '%s: %s' % (EventHTMLFormater.bold(EventHTMLFormater.blue('Change Encounter')), EventHTMLFormater.green('Enabled'))


class Command201Formater(object):

    """Transfer Player"""

    @staticmethod
    def formatCommand(params):
        f = {}
        f['appoint'] = params[0]
        f['map_id'] = params[1]
        f['x_coord'] = params[2]
        f['y_coord'] = params[3]
        direction = {0: 'Retain', 2: 'Down', 4: 'Left', 6: 'Right', 8: 'Up'}
        f['direction'] = direction[params[4]]
        boolean_dict = {0: 'True', 1: 'False'}
        f['fade'] = boolean_dict[params[5]]
        return Command201Formater.template(f)

    @staticmethod
    def template(f):
        template = '%s: ' % (EventHTMLFormater.blue('Transfer Player'))
        if f['appoint'] == 0:
            template += 'Map ID (%s) at (%s, %s), ' % (EventHTMLFormater.red('%(map_id)s'),
                                                       EventHTMLFormater.blue('%(x_coord)s'), EventHTMLFormater.blue('%(y_coord)s'))
        else:
            template += '[Variables] Map ID ([%s]) at ([%s], [%s]), ' % (EventHTMLFormater.red('%(map_id)04d'),
                                                                         EventHTMLFormater.blue('%(x_coord)04d'), EventHTMLFormater.blue('%(y_coord)04d'))

        template += 'Direction %s %s, Fade %s %s' % (EventHTMLFormater.bold('='), EventHTMLFormater.italic('%(direction)s'),
                                                     EventHTMLFormater.bold('='), EventHTMLFormater.blue(EventHTMLFormater.bold('%(fade)s')))
        return template % f


class Command202Formater(object):

    """Set Event Location"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command202Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command203Formater(object):

    """Scroll Map"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command203Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command204Formater(object):

    """Change Map Settings"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command204Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command205Formater(object):

    """Change Fog Color Tone"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command205Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command206Formater(object):

    """Change Fog Opacity"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command206Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command207Formater(object):

    """Show Animation"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command207Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command208Formater(object):

    """Change Transparent Flag"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command208Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command209Formater(object):

    """Set Move Route"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command209Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command210Formater(object):

    """Wait for Move's Completion"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command210Formater.template(f)

    @staticmethod
    def template(f):
        return '%s' % (EventHTMLFormater.bold('Wait for Move\'s Completion'))


class Command221Formater(object):

    """Prepare for Transition"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command221Formater.template(f)

    @staticmethod
    def template(f):
        return '%s' % (EventHTMLFormater.bold('Prepare for Transition'))


class Command222Formater(object):

    """Execute Transition"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command222Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command223Formater(object):

    """Change Screen Color Tone"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command223Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command224Formater(object):

    """Screen Flash"""

    @staticmethod
    def formatCommand(params):
        f = {}
        f['params'] = params
        f['screen_color'] = params[0]
        f['screen_time'] = params[1]
        return Command224Formater.template(f)

    @staticmethod
    def template(f):
        template = "%s %s %s %s %s" % (
            EventHTMLFormater.color('#808000', 'Screen Flash:'),
            EventHTMLFormater.colorObj(f['screen_color']),
            EventHTMLFormater.blue(EventHTMLFormater.bold('in')),
            EventHTMLFormater.red('%(screen_time)s'),
            EventHTMLFormater.color('#808000', 'Frames')
        )
        return template % f


class Command225Formater(object):

    """Screen Shake"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command225Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command231Formater(object):

    """Show Picture"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command231Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command232Formater(object):

    """Move Picture"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command232Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command233Formater(object):

    """Rotate Picture"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command233Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command234Formater(object):

    """Change Picture Color Tone"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command234Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command235Formater(object):

    """Erase Picture"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command235Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command236Formater(object):

    """Set Weather Effects"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command236Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command241Formater(object):

    """Play BGM"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command241Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command242Formater(object):

    """Fade Out BGM"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command242Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command245Formater(object):

    """Play BGS"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command245Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command246Formater(object):

    """Fade Out BGS"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command246Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command247Formater(object):

    """Memorize BGM/BGS"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command247Formater.template(f)

    @staticmethod
    def template(f):
        return '%s' % (EventHTMLFormater.bold('Memorize BGM/BGS'))


class Command248Formater(object):

    """Restore BGM/BGS"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command248Formater.template(f)

    @staticmethod
    def template(f):
        return '%s' % (EventHTMLFormater.bold('Restore BGM/BGS'))


class Command249Formater(object):

    """Play ME"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command249Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command250Formater(object):

    """Play SE"""

    @staticmethod
    def formatCommand(params):
        f = {}
        f['params'] = params
        f['se_file'] = params[0]
        return Command250Formater.template(f)

    @staticmethod
    def template(f):
        template = '%s %s' % (
            EventHTMLFormater.color('#348781', 'Play SE:'),
            EventHTMLFormater.audioFile(f['se_file'])
        )
        return template % f


class Command251Formater(object):

    """Stop SE"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command251Formater.template(f)

    @staticmethod
    def template(f):
        return '%s' % (EventHTMLFormater.bold('Stop SE'))


class Command301Formater(object):

    """Battle Processing"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command301Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command601Formater(object):

    """If Win"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command601Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command602Formater(object):

    """If Escape"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command602Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command603Formater(object):

    """If Lose"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command603Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command302Formater(object):

    """Shop Processing"""

    @staticmethod
    def formatCommand(params):
        f = {}
        f['params'] = params
        f['shop_item_type'] = params[0]
        project = Kernel.GlobalObjects["PROJECT"]
        if params[0] == 0:
            items = project.getData('Items')
            f['shop_item'] = items[params[1]]
        elif params[0] == 1:
            weapons = project.getData('Weapons')
            f['shop_item'] = weapons[params[1]]
        elif params[0] == 2:
            armors = project.getData('Armors')
            f['shop_item'] = armors[params[1]]
        else:
            pass
        return Command302Formater.template(f)

    @staticmethod
    def template(f):
        if f['shop_item_type'] == 0:
            item = EventHTMLFormater.item(f['shop_item'])
        elif f['shop_item_type'] == 1:
            item = EventHTMLFormater.weapon(f['shop_item'])
        elif f['shop_item_type'] == 2:
            item = EventHTMLFormater.armor(f['shop_item'])
        else:
            item = EventHTMLFormater.red(EventHTMLFormater.bold(
                'Error:') + (' Unknown Item type [%s]' % f['shop_item_type']))
        template = '%s %s' % (
            EventHTMLFormater.color('#F88017', 'Shop:'),
            item
        )
        return template


    @staticmethod
    def template(f):
        if f['shop_item_type'] == 0:
            item = EventHTMLFormater.item(f['shop_item'])
        elif f['shop_item_type'] == 1:
            item = EventHTMLFormater.weapon(f['shop_item'])
        elif f['shop_item_type'] == 2:
            item = EventHTMLFormater.armor(f['shop_item'])
        else:
            item = EventHTMLFormater.red(EventHTMLFormater.bold(
                'Error:') + (' Unknown Item type [%s]' % f['shop_item_type']))
        template = '%s %s' % (
            EventHTMLFormater.color('#F88017', '&nbsp;&nbsp;&nbsp;&nbsp;:'),
            item
        )
        return template


class Command303Formater(object):

    """Name Input Processing"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command303Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command311Formater(object):

    """Change HP"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command311Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command312Formater(object):

    """Change SP"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command312Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command313Formater(object):

    """Change State"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command313Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command314Formater(object):

    """Recover All"""

    @staticmethod
    def formatCommand(params):
        f = {}
        project = Kernel.GlobalObjects["PROJECT"]
        actors = project.getData('Actors')
        f['params'] = params
        f['actor_id'] = params[0]
        if params[0] > 0:
            f['actor_name'] = actors[params[0]].name
        return Command314Formater.template(f)

    @staticmethod
    def template(f):
        if f['actor_id'] <= 0:
            actor = 'Entire Party'
        else:
            actor = 'Actor [%s: %s]' % (
                EventHTMLFormater.red('%(actor_id)03d'), EventHTMLFormater.green('%(actor_name)s'))
        template = '%s %s' % (
            EventHTMLFormater.color('#3BB9FF', 'Recover All:'),
            actor
        )
        return template % f


class Command315Formater(object):

    """Change EXP"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command315Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command316Formater(object):

    """Change Level"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command316Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command317Formater(object):

    """Change Parameters"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command317Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command318Formater(object):

    """Change Skills"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command318Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command319Formater(object):

    """Change Equipment"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command319Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command320Formater(object):

    """Change Actor Name"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command320Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command321Formater(object):

    """Change Actor Class"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command321Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command322Formater(object):

    """Change Actor Graphic"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command322Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command331Formater(object):

    """Change Enemy HP"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command331Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command332Formater(object):

    """Change Enemy SP"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command332Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command333Formater(object):

    """Change Enemy State"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command333Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command334Formater(object):

    """Enemy Recover All"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command334Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command335Formater(object):

    """Enemy Appearance"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command335Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command336Formater(object):

    """Enemy Transform"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command336Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command337Formater(object):

    """Show Battle Animation"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command337Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command338Formater(object):

    """Deal Damage"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command338Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command339Formater(object):

    """Force Action"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command339Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command340Formater(object):

    """Abort Battle"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command340Formater.template(f)

    @staticmethod
    def template(f):
        return '%s' % (EventHTMLFormater.bold('Abort Battle'))


class Command351Formater(object):

    """Call Menu Screen"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command351Formater.template(f)

    @staticmethod
    def template(f):
        return '%s' % (EventHTMLFormater.bold('Call Menu Screen'))


class Command352Formater(object):

    """Call Save Screen"""

    @staticmethod
    def formatCommand(params):
        f = {}
        f['params'] = params
        return Command352Formater.template(f)

    @staticmethod
    def template(f):
        return EventHTMLFormater.color('#2C3539', 'Call Save Screen:')


class Command353Formater(object):

    """Game Over"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command353Formater.template(f)

    @staticmethod
    def template(f):
        return '%s' % (EventHTMLFormater.bold(EventHTMLFormater.red('Game Over')))


class Command354Formater(object):

    """Return to Title Screen"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command354Formater.template(f)

    @staticmethod
    def template(f):
        return '%s' % (EventHTMLFormater.bold('Return to Title Screen'))


class Command355Formater(object):

    """Script"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command355Formater.template(f)

    @staticmethod
    def template(f):
        return ''


class Command412Formater(object):

    """Conditional Branch End"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command412Formater.template(f)

    @staticmethod
    def template(f):
        return EventHTMLFormater.blue('Branch End')


class Command404Formater(object):

    """Show Choices Branch End"""

    @staticmethod
    def formatCommand(params):
        f = {}
        return Command404Formater.template(f)

    @staticmethod
    def template(f):
        return EventHTMLFormater.blue('Choices End')


class Command605Formater(object):

    """Shop Goods Extra Line"""

    @staticmethod
    def formatCommand(params):
        f = {}
        f['params'] = params
        f['shop_item_type'] = params[0]
        project = Kernel.GlobalObjects["PROJECT"]
        if params[0] == 0:
            items = project.getData('Items')
            f['shop_item'] = items[params[1]]
        elif params[0] == 1:
            weapons = project.getData('Weapons')
            f['shop_item'] = weapons[params[1]]
        elif params[0] == 2:
            armors = project.getData('Armors')
            f['shop_item'] = armors[params[1]]
        else:
            pass
        return Command605Formater.template(f)
