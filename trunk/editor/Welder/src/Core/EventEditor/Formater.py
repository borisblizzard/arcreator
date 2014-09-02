from Boot import WelderImport

Kernel             = WelderImport('Kernel')
Manager            = Kernel.Manager
Type               = Kernel.Type
SuperType          = Kernel.SuperType
Component          = Kernel.Component
Package            = Kernel.Package
KM = Kernel.Manager

class EventCommandFormater(object):
    '''Formats event commands into HTML for display'''

    @staticmethod
    def format(command):
        html = ""
        formater = EventCommandFormater.get_event_formater(command.code).object
        if formater is None:
            return ''.join(("&nbsp;" * 4 * command.indent, '<font color="red"><b>ERROR:</b> No Handeler for event code [%s]</font>' % command.code))
        format = formater.format(command.parameters)
        template = formater.template(format)
        if template == "":
            return ''.join(("&nbsp;" * 4 * command.indent, '<font color="red"><b>ERROR:</b> Event code [%s] defined but not implemented</font>' % command.code))
        return ''.join(("&nbsp;" * 4 * command.indent, template))

    @staticmethod
    def get_event_formater(code):
        name = "Command%03d" % code
        return KM.get_type("EventFormaterType").get_type(name).get_default_component()


class Format(object):

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
        template = Format.color('black', '<b>Color</b>(%s, %s, %s, %s)')
        colors = (
            Format.red('%3d'),
            Format.green('%3d'),
            Format.blue('%3d'),
            Format.bold('%3d')
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
        template = Format.color('black', '<b>Audio</b>{:name => %s, :volume => %s, :pitch => %s}')
        colors = (
            Format.green('%s'),
            Format.red('%3d'),
            Format.red('%3d')
        )
        data = (
            audiofile.name,
            audiofile.volume,
            audiofile.pitch
        )
        return (template % colors) % data

    @staticmethod
    def item(item):
        template = Format.color('black', 'Item [%s: %s]')
        colors = (Format.red('%03d'), Format.green('%s'))
        data = (item.id, item.name)
        return (template % colors) % data

    @staticmethod
    def weapon(weapon):
        template = Format.color('black', 'Weapon [%s: %s]')
        colors = (Format.red('%03d'), Format.green('%s'))
        data = (weapon.id, weapon.name)
        return (template % colors) % data

    @staticmethod
    def armor(armor):
        template = Format.color('black', 'Armor [%s: %s]')
        colors = (Format.red('%03d'), Format.green('%s'))
        data = (armor.id, armor.name)
        return (template % colors) % data


class Command000(object):
    """place holder"""

    @staticmethod
    def format(params):
        format = {}
        format['params'] = params
        return format

    @staticmethod
    def template(format):
        return Format.color('#0000A0', Format.bold('@>'))


class Command101(object):
    """Show Text"""

    @staticmethod
    def format(params):
        format = {}
        format['text'] = params[0]
        return format

    @staticmethod
    def template(format):
        template = '%s %s' % (Format.green('Text:'), Format.italic('%(text)s'))
        return template % format


class Command401(object):
    """Show Text Extra Lines"""

    @staticmethod
    def format(params):
        format = {}
        format['text'] = params[0]
        return format

    @staticmethod
    def template(format):
        template = '&nbsp;&nbsp;&nbsp;&nbsp;%s %s' % (Format.green(':'), Format.italic('%(text)s'))
        return template % format


class Command102(object):
    """Show Choices"""

    @staticmethod
    def format(params):
        format = {}
        format['choice_number'] = len(params[0])
        format['choice_choices'] = params[0]
        format['choice_default'] = params[1]
        return format

    @staticmethod
    def template(format):
        choices = ''
        for i in range(format['choice_number']):
            choices += '(%s)%s' % (Format.red(i), Format.green(format['choice_choices'][i]))
            if i < format['choice_number'] - 1:
                choices += ', '
        format['choice_text'] = choices
        template = ('%s ' * 5) % (
                                  Format.color('#25383C', 'Show Choices:'),
                                  Format.blue(Format.bold(' Case')),
                                  Format.italic('[%(choice_text)s]'),
                                  Format.blue(Format.bold('Default')),
                                  Format.red('%(choice_default)d')
                                 )
        return template % format


class Command402(object):
    """When [**] The command that serves as an entry point for each potential choice"""

    @staticmethod
    def format(params):
        format = {}
        format['choice_name'] = params[1]
        format['choice_id'] = params[0]
        return format

    @staticmethod
    def template(format):
        template = '&nbsp;&nbsp;%s (%s)%s' % (Format.blue(Format.bold('When')), Format.red('%(choice_id)s'), Format.green('%(choice_name)s'))
        return template % format


class Command403(object):
    """When Cancel Choices"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):  
        return '&nbsp;&nbsp;%s %s' % (Format.blue(Format.bold('When')), Format.green('Cancel'))


class Command103(object):
    """Input Number"""

    @staticmethod
    def format(params):
        project = Kernel.GlobalObjects.get_value("PROJECT")
        system = project.getData('System')
        format = {}
        format['variable_id'] = params[0]
        format['variable_name'] = system.variables[params[0]]
        format['digits'] = params[1]
        return format

    @staticmethod
    def template(format):
        template = '%s Variable[%s: %s], (%s digit(s))' % (Format.blue('Input Number:'),
            Format.red('%(variable_id)04d'),
            Format.green('%(variable_name)s'),
            Format.bold('%(digits)s'))
        return template % format


class Command104(object):
    """Change Text Options"""

    @staticmethod
    def format(params):
        format = {}
        pos_dict = {
            0: 'Top',  1: 'Middle', 2: 'Bottom'
        }
        visible_dict = {
            0: 'Show',  1: 'Hide'
        }
        format['msg_pos'] = pos_dict[params[0]]
        format['msg_frame'] = visible_dict[params[1]]
        return format

    @staticmethod
    def template(format):
        template = '%s [%s, %s]' % (Format.italic('Change Text Options:'), Format.bold('%(msg_pos)s'), Format.bold('%(msg_frame)s'))
        return template % format


class Command105(object):
    """Button Input Processing"""

    @staticmethod
    def format(params):
        project = Kernel.GlobalObjects.get_value("PROJECT")
        system = project.getData('System')

        format = {}
        format['var_id'] = params[0]
        format['var_name'] = system.variables[params[0]]
        return format

    @staticmethod
    def template(format):
        template = '%s Variable[%s: %s]' % (Format.bold(Format.red('Button Input Processing: ')), Format.red('%(var_id)04d'), Format.green('%(var_name)s'))
        return template % format


class Command106(object):
    """Wait"""

    @staticmethod
    def format(params):
        format = {}
        format['frames'] = params[0]
        return format

    @staticmethod
    def template(format):
        template = '%s %s %s' % (Format.blue(Format.bold('Wait:')), Format.red('%(frames)s'), Format.red('Frame(s)'))
        return template % format


class Command108(object):
    """Comment"""

    @staticmethod
    def format(params):
        format = {}
        format['text'] = params[0]
        return format

    @staticmethod
    def template(format):
        template = '%s %s' % (Format.green('Comment:'), Format.italic(Format.green('%(text)s')))
        return template % format


class Command408(object):
    """Comment Extra Lines"""

    @staticmethod
    def format(params):
        format = {}
        format['text'] = params[0]
        return format

    @staticmethod
    def template(format):
        template = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%s %s' % (Format.green(':'), Format.italic(Format.green('%(text)s')))
        return template % format


class Command111(object):
    """Conditional Branch"""

    @staticmethod
    def format(params):
        format = {}
        mode = params[0]
        mode_dict = {
            0: 'Switch',  1: 'Variable', 2: 'Self Switch', 3: 'Timer',
            4: 'Actor', 5: 'Enemy', 6: 'character', 7: 'Gold', 8: 'Item',
            9: 'Weapon', 10: 'Armor', 11: 'Button', 12: 'Script'
        }
        format['mode'] = mode
        format['mode_name'] = mode_dict[params[0]]

        project = Kernel.GlobalObjects.get_value("PROJECT")
        system = project.getData('System')

        if mode == 0:  # switch
            format['switch_id'] = params[1]
            format['switch_name'] = system.switches[params[1]]
            if params[2] == 0:
                format['switch_state'] = 'True'
            else:
                format['switch_state'] = 'False'
        elif mode == 1:  # variable
            format['var_one_id'] = params[1]
            format['var_one_name'] = system.variables[params[1]]
            format['var_two_mode'] = params[2]
            if params[2] == 0:
                format['var_two_value'] = params[3]
            else:
                format['var_two_id'] = params[3]
                format['var_two_name'] = system.variables[params[3]]
            operation_dict = {0: '==', 1: '>=', 2: '<=', 3: '>', 4: '<', 5: '!='}
            format['operation'] = operation_dict[params[4]]
        elif mode == 2:  # self switch
            format['self_switch'] = params[1]
            if params[2] == 0:
                format['switch_state'] = 'True'
            else:
                format['switch_state'] = 'False'
        elif mode == 3:  # timer
            format['time'] = params[1]
            format['time_mode'] = params[2]
        elif mode == 4:  # actor
            actors = project.getData('Actors')
            format['actor_id'] = params[1]
            format['actor_name'] = actors[params[1]].name
            format['actor_mode'] = params[2]
            if params[2] == 1:  # name
                format['actor_condition_name'] = params[3]
            elif params[2] == 2:  # skill
                skills = project.getData('Skills')
                format['skill_id'] = params[3]
                format['skill_name'] = skills[params[3]].name
            elif params[2] == 3:  # weapon
                weapons = project.getData('Weapons')
                format['weapon_id'] = params[3]
                format['weapon_name'] = weapons[params[3]].name
            elif params[2] == 4:  # armor
                armors = project.getData('Armors')
                format['armor_id'] = params[3]
                format['armor_name'] = armors[params[3]].name
            elif params[2] == 5:  # state
                states = project.getData('States') #system.states
                format['state_id'] = params[3]
                format['state_name'] = states[params[3]].name
            if params[2] != 0:
                format['actor_condition'] = params[3]
        elif mode == 5:  # enemy
            format['enemy_position'] = params[1]
            format['enemy_mode'] = params[2]
            format['enemy_state_id'] = params[3]
            format['enemy_state_name'] = system.states[params[3]]
        elif mode == 6:  # character
            format['character_id'] = params[1]
            format['character_direction'] = params[2]
        elif mode == 7:  # gold
            format['gold_mode'] = params[2]
            format['gold_value'] = params[1]
        elif mode == 8:  # item
            items = project.getData('Items')
            format['item_id'] = params[1]
            format['item_name'] = items[params[1]].name
        elif mode == 9:  # weapon
            weapons = project.getData('Weapons')
            format['weapon_id'] = params[1]
            format['weapon_name'] = weapons[params[1]].name
        elif mode == 10:  # armor
            armors = project.getData('Armors')
            format['armor_id'] = params[1]
            format['armor_name'] = armors[params[1]].name
        elif mode == 11:  # button
            format['button'] = params[1]
        elif mode == 12:
            format['script'] = params[1]
        else:
            pass

        return format

    @staticmethod
    def template(format):
        mode = format['mode']
        template = (Format.blue('Conditional Branch: %s') % Format.bold('if')) + ' %s'
        html = (Format.red('%s Missing handeler for mode [%s]') % (Format.bold('ERROR[Code 111: Conditional Branch]:'), '%(mode)s')) % format
        if mode == 0:  # switch
            html = (Format.color('black', 'Switch [%s: %s] %s %s') % (
                Format.red('%(switch_id)04d'),
                Format.green('%(switch_name)s'),
                Format.bold('=='),
                Format.blue(Format.bold('%(switch_state)s'))
            )) % format
        elif mode == 1:  # variable
            if format['var_two_mode'] == 0:
                html = ('Variable [%s: %s] %s %s' % (
                    Format.red('%(var_one_id)04d'),
                    Format.green('%(var_one_name)s'),
                    Format.bold('%(operation)s'),
                    Format.bold('%(var_two_value)s')
                )) % format
            else:
                html = ('Variable [%s: %s] %s Variable [%s: %s]' % (
                    Format.red('%(var_one_id)04d'),
                    Format.green('%(var_one_name)s'),
                    Format.bold('%(operation)s'),
                    Format.red('%(var_two_id)04d'),
                    Format.green('%(var_two_name)s')
                )) % format
        elif mode == 2:  # self switch
            html = ('Self Switch %s %s %s' % (
                Format.green('%(self_switch)s'),
                Format.bold('=='),
                Format.green('%(switch_state)s')
            )) % format
        elif mode == 3:  # timer
            if format['time_mode'] == 0:
                html = ('Timer %s %s seconds' % (Format.bold('>='), Format.red('%(time)s'))) % format
            else:
                html = ('Timer %s %s seconds' % (Format.bold("<="), Format.red('%(time)s'))) % format
        elif mode == 4:  # actor
            if format['actor_mode'] == 0:  # in party
                html = ('Actor [%s: %s] %s in party' % (
                    Format.red('%(actor_id)s'),
                    Format.green('%(actor_name)s'),
                    Format.bold('is')
                )) % format
            elif format['actor_mode'] == 1:  # name
                html = ('Actor [%s: %s] %s %s' % (
                    Format.red('%(actor_id)s'), 
                    Format.green('%(actor_name)s'), 
                    Format.bold('=='), 
                    Format.green('%(actor_condition_name)s')
                )) % format
            elif format['actor_mode'] == 2:  # skill
                html = ('Actor [%s: %s] Has Skill [%s: %s]' % (
                    Format.red('%(actor_id)s'),
                    Format.green('%(actor_name)s'),
                    Format.red('%(skill_id)04d'),
                    Format.green('%(skill_name)s')
                )) % format
            elif format['actor_mode'] == 3:  # weapon
                html = ('Actor [%s: %s] Has Weapon Equiped [%s: %s]' % (
                    Format.red('%(actor_id)s'),
                    Format.green('%(actor_name)s'),
                    Format.red('%(weapon_id)04d'),
                    Format.green('%(weapon_name)s')
                )) % format
            elif format['actor_mode'] == 4:  # armor
                html = ('Actor [%s: %s] Has Armor Equiped [%s: %s]' % (
                    Format.red('%(actor_id)s'),
                    Format.green('%(actor_name)s'),
                    Format.red('%(armor_id)04d'),
                    Format.green('%(armor_name)s')
                )) % format
            elif format['actor_mode'] == 5:  # state
                html = ('Actor [%s: %s] Has State [%s: %s]' % (
                    Format.red('%(actor_id)s'),
                    Format.green('%(actor_name)s'),
                    Format.red('%(state_id)04d'),
                    Format.green('%(state_name)s')
                )) % format
        elif mode == 5:  # enemy
            if format['enemy_mode'] == 0:  # appear
                html = ('Enemy at positon [%s] Appears' % Format.red('%(enemy_position)s')) % format
            elif format['enemy_mode'] == 1:  # state
                html = ('Enemy at positon [%s] Has State [%s: %s]' % (
                    Format.red('%(enemy_position)s'), 
                    Format.red('%(enemy_state_id)04d'), 
                    Format.green('%(enemy_state_name)s')
                )) % format
        elif mode == 6:  # character
            directionmap = {
                2: 'DOWN',
                4: 'LEFT',
                6: 'RIGHT',
                8: 'UP'
            }
            format['character_direction_name'] = directionmap[format['character_direction']]
            if format['character_id'] == -1:
                html = ('Player %s Facing %s' % (Format.bold('is'), Format.green('%(character_direction_name)s'))) % format
            elif format['character_id'] == 0:
                html = ('This Event %s Facing %s' % (Format.bold('is'), Format.green('%(character_direction_name)s'))) % format
            else:
                html = ('Event ID [%s] <b>is</b> Facing %(character_direction_name)s' % (
                    Format.red('%(character_id)04d'),
                    Format.bold('is'),
                    Format.green('%(character_direction_name)s')
                )) % format
        elif mode == 7:  # gold
            if format['gold_mode'] == 0:
                html = ('Party Gold %s %s' % (Format.bold('>='), Format.red('%(gold_value)s'))) % format
            else:
                html = ('Party Gold %s %s' % (Format.bold('<='), Format.red('%(gold_value)s'))) % format
        elif mode == 8:  # item
            html = ('Party Has At Least One of Item [%s: %s]' % (Format.red('%(item_id)04d'), Format.green('%(item_name)s'))) % format
        elif mode == 9:  # weapon
            html = ('Party Has At Least One of Weapon [%s: %s]' % (Format.red('%(weapon_id)04d'), Format.green('%(weapon_name)s'))) % format
        elif mode == 10:  # armor
            html = ('Party Has At Least One of Armor [%s: %s]' % (Format.red('%(armor_id)04d'), Format.green('%(armor_name)s'))) % format
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
            format['button_name'] = buttonmap[format['button']]
            html = ('Button [%s] %s Pressed' % (Format.red('%(button_name)s'), Format.bold('is'))) % format
        else:  # script
            html = 'Script: '
            lines = format['script'].split('\n')
            html += Format.italic(Kernel.escapeHTML(lines[0]))

        body = template % html
        return body


class Command411(object):
    """Else"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return '%s' %  (Format.blue('Else'))


class Command112(object):
    """Loop"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return '%s' % (Format.blue('Loop'))


class Command413(object):
    """Repeat Above"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return '%s' % (Format.blue('Repeat Above'))


class Command113(object):
    """Break Loop"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return '%s' % (Format.blue('Break Loop'))


class Command115(object):
    """Exit Event Processing"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return '%s' % (Format.red(Format.bold('Exit Event Processing')))


class Command116(object):
    """Erase Event"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return '%s' % (Format.red(Format.bold('Erase Event')))


class Command117(object):
    """Call Common Event"""

    @staticmethod
    def format(params):
        format = {}
        format['commonevent_id'] = params[0]
        return format

    @staticmethod
    def template(format):
        template = '%s: ID [%s]' % (Format.red('Call Common Event'), Format.red(Format.bold('%(commonevent_id)s')))
        return template % format


class Command118(object):
    """Label"""

    @staticmethod
    def format(params):
        format = {}
        format['label_name'] = params[0]
        return format

    @staticmethod
    def template(format):
        template = '%s: %s' % (Format.blue('Label'), Format.green('%(label_name)s'))
        return template % format


class Command119(object):
    """Jump to Label"""

    @staticmethod
    def format(params):
        format = {}
        format['jump_to_name'] = params[0]
        return format

    @staticmethod
    def template(format):
        template = '%s: %s' % (Format.blue('Jump to Label'), Format.green(Format.italic('%(jump_to_name)s')))
        return template % format


class Command121(object):
    """Control Switches"""

    @staticmethod
    def format(params):
        format = {}
        project = Kernel.GlobalObjects.get_value("PROJECT")
        system = project.getData('System')
        format['params'] = params
        format['switch_1_id'] = params[0]
        format['switch_1_name'] = system.switches[params[0]]
        format['switch_2_id'] = params[1]
        format['switch_2_name'] = system.switches[params[1]]
        if params[2] == 0:
            format['switch_state'] = 'True'
        else:
            format['switch_state'] = 'False'
        return format

    @staticmethod
    def template(format):
        if format['switch_2_id'] == format['switch_1_id']:  # only modifying 1 var
            template = '%s Switch [%s: %s] = %s' % (
                Format.red('Control Switch:'),
                Format.red('%(switch_1_id)s'),
                Format.green('%(switch_1_name)s'),
                Format.blue(Format.bold('%(switch_state)s'))
            )
        else:
            template = '%s [%s: %s] -> [%s:%s] = %s' % (
                Format.red('Control Switchs:'),
                Format.red('%(switch_1_id)s'),
                Format.green('%(switch_1_name)s'),
                Format.red('%(switch_2_id)s'),
                Format.green('%(switch_2_name)s'),
                Format.blue(Format.bold('%(switch_state)s'))
            )
        return template % format


class Command122(object):
    """Control Variables"""

    @staticmethod
    def format(params):
        format = {}
        format['batch_low'] = params[0]
        format['batch_high'] = params[1]

        operator_dict = {
            0: '= ', 1: '+= ', 2: '-= ', 3: '*= ', 4: '/= ', 5: '%= '
        }
        format['operation'] = operator_dict[params[2]]
        format['operand'] = params[3]

        if(params[4] & 0x80000000):
            format['op_param1'] = -0x100000000 + params[4]
        else:
            format['op_param1'] = params[4]

        if params[3] == 2 or params[3] == 4 or params[3] == 5 or params[3] == 6:
            if(params[5] & 0x80000000):
                format['op_param2'] = -0x100000000 + params[5]
            else:
                format['op_param2'] = params[5]

        return format

    @staticmethod
    def template(format):
        template = '%s: ' % (Format.red('Control Variables'))
        project = Kernel.GlobalObjects.get_value("PROJECT")
        system = project.getData('System')
        # Draw variable or batch
        if format['batch_low'] == format['batch_high']:
            format['var_name'] = system.variables[format['batch_low']]
            template += '[%s: %s] ' % (Format.bold('%(batch_low)04d'), Format.red('%(var_name)s'))
        else:
            template += '[%s..%s] ' % (Format.red('%(batch_low)04d'), Format.red('%(batch_high)04d'))
        # Draw operation symbol
        template += '%s' % (Format.red('%(operation)s'))
        # Draw operand
        if format['operand'] == 0: # constant
            template += '%s' % (Format.red(Format.italic('%(op_param1)s')))
        elif format['operand'] == 1: # variable
            format['opr_var_name'] = system.variables[format['op_param1']]
            template += '[%s: %s] ' % (Format.bold('%(op_param1)04d'), Format.red('%(opr_var_name)s'))
        elif format['operand'] == 2: # random number
            template += '%s(%s, %s)' % (Format.bold('rand'), Format.red('%(op_param1)s'), Format.red('%(op_param2)s'))
        elif format['operand'] == 3: # item
            items = project.getData('Items')
            format['item_name'] = items[format['op_param1']].name
            template += '[%s: %s] In Inventory' % (Format.red('%(op_param1)04d'), Format.red('%(item_name)s'))
        elif format['operand'] == 4: # actor
            actors = project.getData('Actors')
            format['actor_name'] = actors[format['op_param1']].name
            template += '[%s: %s].' % (Format.red('%(op_param1)04d'), Format.red('%(actor_name)s'))
            if format['op_param2'] == 0: # Level
                template += '%s' % (Format.bold('level'))
            elif format['op_param2'] == 1: # EXP
                template += '%s' % (Format.bold('exp'))
            elif format['op_param2'] == 2: # HP
                template += '%s' % (Format.bold('hp'))
            elif format['op_param2'] == 3: # SP
                template += '%s' % (Format.bold('sp'))
            elif format['op_param2'] == 4: # MaxHP
                template += '%s' % (Format.bold('maxhp'))
            elif format['op_param2'] == 5: # MaxSP
                template += '%s' % (Format.bold('maxsp'))
            elif format['op_param2'] == 6: # STR
                template += '%s' % (Format.bold('str'))
            elif format['op_param2'] == 7: # DEX
                template += '%s' % (Format.bold('dex'))
            elif format['op_param2'] == 8: # AGI
                template += '%s' % (Format.bold('agi'))
            elif format['op_param2'] == 9: # INT
                template += '%s' % (Format.bold('int'))
            elif format['op_param2'] == 10: # ATK
                template += '%s' % (Format.bold('atk'))
            elif format['op_param2'] == 11: # PDEF
                template += '%s' % (Format.bold('pdef'))
            elif format['op_param2'] == 12: # MDEF
                template += '%s' % (Format.bold('mdef'))
            elif format['op_param2'] == 13: # EVA
                template += '%s' % (Format.bold('eva'))
        elif format['operand'] == 5: # enemy
            template += 'Enemy at positon [%s].' % (Format.red('%(op_param1)s'))
            if format['op_param2'] == 0:
                template += '%s' % (Format.bold('hp'))
            elif format['op_param2'] == 1: # SP
                template += '%s' % (Format.bold('sp'))
            elif format['op_param2'] == 2: # MaxHP
                template += '%s' % (Format.bold('maxhp'))
            elif format['op_param2'] == 3: # MaxSP
                template += '%s' % (Format.bold('maxsp'))
            elif format['op_param2'] == 4: # STR
                template += '%s' % (Format.bold('str'))
            elif format['op_param2'] == 5: # DEX
                template += '%s' % (Format.bold('dex'))
            elif format['op_param2'] == 6: # AGI
                template += '%s' % (Format.bold('agi'))
            elif format['op_param2'] == 7: # INT
                template += '%s' % (Format.bold('int'))
            elif format['op_param2'] == 8: # PDEF
                template += '%s' % (Format.bold('pdef'))
            elif format['op_param2'] == 9: # MDEF
                template += '%s' % (Format.bold('mdef'))
            elif format['op_param2'] == 10: # EVA
                template += '%s' % (Format.bold('eva'))
        elif format['operand'] == 6: # character
            if format['op_param1'] == -1: # player
                template += '[Player].'
            elif format['op_param1'] == 0: # this event
                template += '[This Event].'
            else:
                template += 'Event[%s].' % (Format.red('%(op_param1)04d'))
            # Choice
            if format['op_param2'] == 0: # Map X
                template += '%s' % (Format.bold('map_x'))
            elif format['op_param2'] == 1: # Map Y
                template += '%s' % (Format.bold('map_y'))
            elif format['op_param2'] == 2: # Direction
                template += '%s' % (Format.bold('direction'))
            elif format['op_param2'] == 3: # Screen X
                template += '%s' % (Format.bold('screen_x'))
            elif format['op_param2'] == 4: # Screen Y
                template += '%s' % (Format.bold('screen_y'))
            elif format['op_param2'] == 5: # Terrain Tag
                template += '%s' % (Format.bold('terrain_tag'))
        elif format['operand'] == 7: # other
            if format['op_param1'] == 0: # Map ID
                template += '%s' % (Format.bold('Map ID'))
            elif format['op_param1'] == 1: # Party Members
                template += '%s' % (Format.bold('Party Members'))
            elif format['op_param1'] == 2: # Gold
                template += '%s' % (Format.bold('Gold'))
            elif format['op_param1'] == 3: # Steps
                template += '%s' % (Format.bold('Steps'))
            elif format['op_param1'] == 4: # Play Time
                template += '%s' % (Format.bold('Play Time'))
            elif format['op_param1'] == 5: # Timer
                template += '%s' % (Format.bold('Timer'))
            elif format['op_param1'] == 6: # Save Count
                template += '%s' % (Format.bold('Save Count'))

        return template % format


class Command123(object):
    """Control Self Switch"""

    @staticmethod
    def format(params):
        format = {}
        format['self_switch'] = params[0]
        if params[1] == 0:
            format['switch_state'] = 'True'
        else:
            format['switch_state'] = 'False'
        return format

    @staticmethod
    def template(format):
        template = '%s: %s %s %s' % (Format.red('Control Self Switch'),
                                     Format.green('%(self_switch)s'),
                                     Format.bold('='),
                                     Format.green('%(switch_state)s'))
        return template % format


class Command124(object):
    """Control Timer"""

    @staticmethod
    def format(params):
        format = {}
        format['timer_state'] = params[0]
        if params[0] == 0:
            format['timer_countdown'] = params[1]
        return format

    @staticmethod
    def template(format):
        if format['timer_state'] == 0:
            template = '%s: %s (%s seconds)' % (Format.bold('Control Timer'), 
                                                Format.red(Format.italic('Start')),
                                                Format.red('%(timer_countdown)s'))
        else:
            template = '%s: %s' % (Format.bold('Control Timer'), Format.red(Format.italic('Stop')))
        return template % format


class Command125(object):
    """Change Gold"""

    @staticmethod
    def format(params):
        format = {}
        operation = {0: '+', 1: '-'}
        format['operation'] = operation[params[0]]
        format['operand_type'] = params[1]
        format['operand'] = params[2]
        return format

    @staticmethod
    def template(format):
        template = '%s: %s' % (Format.italic(Format.green('Change Gold')), Format.bold('%(operation)s'))
        if format['operand_type'] == 0: # constant
            template += '%s' % (Format.bold(Format.red('%(operand)s')))
        else:                           # variable
            project = Kernel.GlobalObjects.get_value("PROJECT")
            system = project.getData('System')
            format['var_name'] = system.variables[format['operand']]
            template += 'Variable [%s: %s]' % (Format.bold('%(operand)04d'), Format.red('%(var_name)s'))
        return template % format


class Command126(object):
    """Change Items"""

    @staticmethod
    def format(params):
        format = {}
        format['item_id'] = params[0]
        operation = {0: '+', 1: '-'}
        format['operation'] = operation[params[1]]
        format['operand_type'] = params[2]
        format['operand'] = params[3]
        return format

    @staticmethod
    def template(format):
        project = Kernel.GlobalObjects.get_value("PROJECT")
        items = project.getData('Items')
        format['item_name'] = items[format['item_id']].name
        template = '%s: [%s: %s], %s' % (Format.italic(Format.green('Change Items')), Format.blue('%(item_id)04d'),
                                         Format.blue('%(item_name)s'), Format.bold('%(operation)s'))
        if format['operand_type'] == 0: # constant
            template += '%s' % (Format.bold(Format.red('%(operand)s')))
        else:                           # variable
            system = project.getData('System')
            format['var_name'] = system.variables[format['operand']]
            template += 'Variable [%s: %s]' % (Format.bold('%(operand)04d'), Format.red('%(var_name)s'))
        return template % format


class Command127(object):
    """Change Weapons"""

    @staticmethod
    def format(params):
        format = {}
        format['weapon_id'] = params[0]
        operation = {0: '+', 1: '-'}
        format['operation'] = operation[params[1]]
        format['operand_type'] = params[2]
        format['operand'] = params[3]
        return format

    @staticmethod
    def template(format):
        project = Kernel.GlobalObjects.get_value("PROJECT")
        weapons = project.getData('Weapons')
        format['weapon_name'] = weapons[format['weapon_id']].name
        template = '%s: [%s: %s], %s' % (Format.italic(Format.green('Change Weapons')), Format.blue('%(weapon_id)04d'),
                                         Format.blue('%(weapon_name)s'), Format.bold('%(operation)s'))
        if format['operand_type'] == 0: # constant
            template += '%s' % (Format.bold(Format.red('%(operand)s')))
        else:                           # variable
            system = project.getData('System')
            format['var_name'] = system.variables[format['operand']]
            template += 'Variable [%s: %s]' % (Format.bold('%(operand)04d'), Format.red('%(var_name)s'))
        return template % format


class Command128(object):
    """Change Armor"""

    @staticmethod
    def format(params):
        format = {}
        format['armor_id'] = params[0]
        operation = {0: '+', 1: '-'}
        format['operation'] = operation[params[1]]
        format['operand_type'] = params[2]
        format['operand'] = params[3]
        return format

    @staticmethod
    def template(format):
        project = Kernel.GlobalObjects.get_value("PROJECT")
        armors = project.getData('Armors')
        format['armor_name'] = armors[format['armor_id']].name
        template = '%s: [%s: %s], %s' % (Format.italic(Format.green('Change Armors')), Format.blue('%(armor_id)04d'),
                                         Format.blue('%(armor_name)s'), Format.bold('%(operation)s'))
        if format['operand_type'] == 0: # constant
            template += '%s' % (Format.bold(Format.red('%(operand)s')))
        else:                           # variable
            system = project.getData('System')
            format['var_name'] = system.variables[format['operand']]
            template += 'Variable [%s: %s]' % (Format.bold('%(operand)04d'), Format.red('%(var_name)s'))
        return template % format


class Command129(object):
    """Change Party Member"""

    @staticmethod
    def format(params):
        format = {}
        format['actor_id'] = params[0]
        project = Kernel.GlobalObjects.get_value("PROJECT")
        actors = project.getData('Actors')
        format['actor_name'] = actors[params[0]].name
        operation = {0: 'Add', 1: 'Remove'}
        format['operation'] = operation[params[1]]
        format['initialize'] = params[2]
        return format

    @staticmethod
    def template(format):
        template = '%s: %s Actor[%s: %s]' % (Format.blue('Change Party Member'), Format.red('%(operation)s'),
                                             Format.red('%(actor_id)04d'), Format.red('%(actor_name)s'))
        if format['initialize'] == 1: #Initialize Actor
            template += ', Initialize'
        return template % format


class Command131(object):
    """Change Windowskin"""

    @staticmethod
    def format(params):
        format = {}
        format['winskin_name'] = params[0]
        return format

    @staticmethod
    def template(format):
        template = '%s: %s' % (Format.bold('Change Windowskin'), Format.green('%(winskin_name)s'))
        return template % format


class Command132(object):
    """Change Battle BGM"""

    @staticmethod
    def format(params):
        format = {}
        format['params'] = params
        format['se_file'] = params[0]
        return format

    @staticmethod
    def template(format):
        template = '%s %s' % (
            Format.color('#348781', 'Change Battle BGM:'),
            Format.audioFile(format['se_file'])
        )
        return template % format


class Command133(object):
    """Change Battle End ME"""

    @staticmethod
    def format(params):
        format = {}
        format['params'] = params
        format['se_file'] = params[0]
        return format

    @staticmethod
    def template(format):
        template = '%s %s' % (
            Format.color('#348781', 'Change Battle End ME:'),
            Format.audioFile(format['se_file'])
        )
        return template % format


class Command134(object):
    """Change Save Access"""

    @staticmethod
    def format(params):
        format = {}
        format['can_save'] = params[0]
        return format

    @staticmethod
    def template(format):
        if format['can_save'] == 0:
             return '%s: %s' % (Format.bold(Format.blue('Change Save Access')), Format.red('Disabled'))
        else:
             return '%s: %s' % (Format.bold(Format.blue('Change Save Access')), Format.green('Enabled'))


class Command135(object):
    """Change Menu Access"""

    @staticmethod
    def format(params):
        format = {}
        format['access_menu'] = params[0]
        return format

    @staticmethod
    def template(format):
        if format['access_menu'] == 0:
             return '%s: %s' % (Format.bold(Format.blue('Change Menu Access')), Format.red('Disabled'))
        else:
             return '%s: %s' % (Format.bold(Format.blue('Change Menu Access')), Format.green('Enabled'))


class Command136(object):
    """Change Encounter"""

    @staticmethod
    def format(params):
        format = {}
        format['can_encounter'] = params[0]
        return format

    @staticmethod
    def template(format):
        if format['can_encounter'] == 0:
             return '%s: %s' % (Format.bold(Format.blue('Change Encounter')), Format.red('Disabled'))
        else:
             return '%s: %s' % (Format.bold(Format.blue('Change Encounter')), Format.green('Enabled'))


class Command201(object):
    """Transfer Player"""

    @staticmethod
    def format(params):
        format = {}
        format['appoint'] = params[0]
        format['map_id'] = params[1]
        format['x_coord'] = params[2]
        format['y_coord'] = params[3]
        direction = {0: 'Retain', 2: 'Down', 4: 'Left', 6: 'Right', 8: 'Up'}
        format['direction'] = direction[params[4]]
        boolean_dict = {0: 'True', 1: 'False'}
        format['fade'] = boolean_dict[params[5]]
        return format

    @staticmethod
    def template(format):
        template = '%s: ' % (Format.blue('Transfer Player'))
        if format['appoint'] == 0:
            template += 'Map ID (%s) at (%s, %s), ' % (Format.red('%(map_id)s'),
                        Format.blue('%(x_coord)s'), Format.blue('%(y_coord)s'))
        else:
            template += '[Variables] Map ID ([%s]) at ([%s], [%s]), ' % (Format.red('%(map_id)04d'),
                        Format.blue('%(x_coord)04d'), Format.blue('%(y_coord)04d'))

        template += 'Direction %s %s, Fade %s %s' % (Format.bold('='), Format.italic('%(direction)s'),
                                                     Format.bold('='), Format.blue(Format.bold('%(fade)s')))
        return template % format


class Command202(object):
    """Set Event Location"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command203(object):
    """Scroll Map"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command204(object):
    """Change Map Settings"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command205(object):
    """Change Fog Color Tone"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command206(object):
    """Change Fog Opacity"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command207(object):
    """Show Animation"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command208(object):
    """Change Transparent Flag"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command209(object):
    """Set Move Route"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command210(object):
    """Wait for Move's Completion"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return '%s' % (Format.bold('Wait for Move\'s Completion'))


class Command221(object):
    """Prepare for Transition"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return '%s' % (Format.bold('Prepare for Transition'))


class Command222(object):
    """Execute Transition"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command223(object):
    """Change Screen Color Tone"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command224(object):
    """Screen Flash"""

    @staticmethod
    def format(params):
        format = {}
        format['params'] = params
        format['screen_color'] = params[0]
        format['screen_time'] = params[1]
        return format

    @staticmethod
    def template(format):
        template = "%s %s %s %s %s" % (
            Format.color('#808000', 'Screen Flash:'),
            Format.colorObj(format['screen_color']),
            Format.blue(Format.bold('in')),
            Format.red('%(screen_time)s'),
            Format.color('#808000', 'Frames')
        )
        return template % format


class Command225(object):
    """Screen Shake"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command231(object):
    """Show Picture"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command232(object):
    """Move Picture"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command233(object):
    """Rotate Picture"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command234(object):
    """Change Picture Color Tone"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command235(object):
    """Erase Picture"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command236(object):
    """Set Weather Effects"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command241(object):
    """Play BGM"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command242(object):
    """Fade Out BGM"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command245(object):
    """Play BGS"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command246(object):
    """Fade Out BGS"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command247(object):
    """Memorize BGM/BGS"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return '%s' % (Format.bold('Memorize BGM/BGS'))


class Command248(object):
    """Restore BGM/BGS"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return '%s' % (Format.bold('Restore BGM/BGS'))


class Command249(object):
    """Play ME"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command250(object):
    """Play SE"""

    @staticmethod
    def format(params):
        format = {}
        format['params'] = params
        format['se_file'] = params[0]
        return format

    @staticmethod
    def template(format):
        template = '%s %s' % (
            Format.color('#348781', 'Play SE:'),
            Format.audioFile(format['se_file'])
        )
        return template % format


class Command251(object):
    """Stop SE"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return '%s' % (Format.bold('Stop SE'))


class Command301(object):
    """Battle Processing"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command601(object):
    """If Win"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command602(object):
    """If Escape"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command603(object):
    """If Lose"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command302(object):
    """Shop Processing"""

    @staticmethod
    def format(params):
        format = {}
        format['params'] = params
        format['shop_item_type'] = params[0]
        project = Kernel.GlobalObjects.get_value("PROJECT")
        if params[0] == 0:
            items = project.getData('Items')
            format['shop_item'] = items[params[1]]
        elif params[0] == 1:
            weapons = project.getData('Weapons')
            format['shop_item'] = weapons[params[1]]
        elif params[0] == 2:
            armors = project.getData('Armors')
            format['shop_item'] = armors[params[1]]
        else:
            pass
        return format

    @staticmethod
    def template(format):
        if format['shop_item_type'] == 0:
            item = Format.item(format['shop_item'])
        elif format['shop_item_type'] == 1:
            item = Format.weapon(format['shop_item'])
        elif format['shop_item_type'] == 2:
            item = Format.armor(format['shop_item'])
        else:
            item = Format.red(Format.bold('Error:') + (' Unknown Item type [%s]' % format['shop_item_type']))
        template = '%s %s' % (
            Format.color('#F88017', 'Shop:'),
            item
        )
        return template


class Command605(object):
    """Shop Goods Extra Line"""

    @staticmethod
    def format(params):
        format = {}
        format['params'] = params
        format['shop_item_type'] = params[0]
        project = Kernel.GlobalObjects.get_value("PROJECT")
        if params[0] == 0:
            items = project.getData('Items')
            format['shop_item'] = items[params[1]]
        elif params[0] == 1:
            weapons = project.getData('Weapons')
            format['shop_item'] = weapons[params[1]]
        elif params[0] == 2:
            armors = project.getData('Armors')
            format['shop_item'] = armors[params[1]]
        else:
            pass
        return format

    @staticmethod
    def template(format):
        if format['shop_item_type'] == 0:
            item = Format.item(format['shop_item'])
        elif format['shop_item_type'] == 1:
            item = Format.weapon(format['shop_item'])
        elif format['shop_item_type'] == 2:
            item = Format.armor(format['shop_item'])
        else:
            item = Format.red(Format.bold('Error:') + (' Unknown Item type [%s]' % format['shop_item_type']))
        template = '%s %s' % (
            Format.color('#F88017', '&nbsp;&nbsp;&nbsp;&nbsp;:'),
            item
        )
        return template


class Command303(object):
    """Name Input Processing"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command311(object):
    """Change HP"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command312(object):
    """Change SP"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command313(object):
    """Change State"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command314(object):
    """Recover All"""

    @staticmethod
    def format(params):
        format = {}
        project = Kernel.GlobalObjects.get_value("PROJECT")
        actors = project.getData('Actors')
        format['params'] = params
        format['actor_id'] = params[0]
        if params[0] > 0:
            format['actor_name'] = actors[params[0]].name
        return format

    @staticmethod
    def template(format):
        if format['actor_id'] <= 0:
            actor = 'Entire Party'
        else:
            actor = 'Actor [%s: %s]' % (Format.red('%(actor_id)03d'), Format.green('%(actor_name)s'))
        template = '%s %s' % (
            Format.color('#3BB9FF', 'Recover All:'),
            actor
        )
        return template % format


class Command315(object):
    """Change EXP"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command316(object):
    """Change Level"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command317(object):
    """Change Parameters"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command318(object):
    """Change Skills"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command319(object):
    """Change Equipment"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command320(object):
    """Change Actor Name"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command321(object):
    """Change Actor Class"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command322(object):
    """Change Actor Graphic"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command331(object):
    """Change Enemy HP"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command332(object):
    """Change Enemy SP"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command333(object):
    """Change Enemy State"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command334(object):
    """Enemy Recover All"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command335(object):
    """Enemy Appearance"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command336(object):
    """Enemy Transform"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command337(object):
    """Show Battle Animation"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command338(object):
    """Deal Damage"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command339(object):
    """Force Action"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command340(object):
    """Abort Battle"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return '%s' % (Format.bold('Abort Battle'))


class Command351(object):
    """Call Menu Screen"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return '%s' % (Format.bold('Call Menu Screen'))


class Command352(object):
    """Call Save Screen"""

    @staticmethod
    def format(params):
        format = {}
        format['params'] = params
        return format

    @staticmethod
    def template(format):
        return Format.color('#2C3539', 'Call Save Screen:')


class Command353(object):
    """Game Over"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return '%s' % (Format.bold(Format.red('Game Over')))


class Command354(object):
    """Return to Title Screen"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return '%s' % (Format.bold('Return to Title Screen'))


class Command355(object):
    """Script"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return ''


class Command412(object):
    """Conditional Branch End"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return Format.blue('Branch End')


class Command404(object):
    """Show Choices Branch End"""

    @staticmethod
    def format(params):
        format = {}
        return format

    @staticmethod
    def template(format):
        return Format.blue('Choices End')


class EventFormaterType(SuperType):

    def __init__(self):
        SuperType.__init__(self, "EventFormaterType")

        Command000 = Type("Command000")
        Command101 = Type("Command101")
        Command401 = Type("Command401")
        Command102 = Type("Command102")
        Command402 = Type("Command402")
        Command403 = Type("Command403")
        Command103 = Type("Command103")
        Command104 = Type("Command104")
        Command105 = Type("Command105")
        Command106 = Type("Command106")
        Command108 = Type("Command108")
        Command408 = Type("Command408")
        Command111 = Type("Command111")
        Command411 = Type("Command411")
        Command112 = Type("Command112")
        Command413 = Type("Command413")
        Command113 = Type("Command113")
        Command115 = Type("Command115")
        Command116 = Type("Command116")
        Command117 = Type("Command117")
        Command118 = Type("Command118")
        Command119 = Type("Command119")
        Command121 = Type("Command121")
        Command122 = Type("Command122")
        Command123 = Type("Command123")
        Command124 = Type("Command124")
        Command125 = Type("Command125")
        Command126 = Type("Command126")
        Command127 = Type("Command127")
        Command128 = Type("Command128")
        Command129 = Type("Command129")
        Command131 = Type("Command131")
        Command132 = Type("Command132")
        Command133 = Type("Command133")
        Command134 = Type("Command134")
        Command135 = Type("Command135")
        Command136 = Type("Command136")
        Command201 = Type("Command201")
        Command202 = Type("Command202")
        Command203 = Type("Command203")
        Command204 = Type("Command204")
        Command205 = Type("Command205")
        Command206 = Type("Command206")
        Command207 = Type("Command207")
        Command208 = Type("Command208")
        Command209 = Type("Command209")
        Command210 = Type("Command210")
        Command221 = Type("Command221")
        Command222 = Type("Command222")
        Command223 = Type("Command223")
        Command224 = Type("Command224")
        Command225 = Type("Command225")
        Command231 = Type("Command231")
        Command232 = Type("Command232")
        Command233 = Type("Command233")
        Command234 = Type("Command234")
        Command235 = Type("Command235")
        Command236 = Type("Command236")
        Command241 = Type("Command241")
        Command242 = Type("Command242")
        Command245 = Type("Command245")
        Command246 = Type("Command246")
        Command247 = Type("Command247")
        Command248 = Type("Command248")
        Command249 = Type("Command249")
        Command250 = Type("Command250")
        Command251 = Type("Command251")
        Command301 = Type("Command301")
        Command601 = Type("Command601")
        Command602 = Type("Command602")
        Command603 = Type("Command603")
        Command302 = Type("Command302")
        Command303 = Type("Command303")
        Command311 = Type("Command311")
        Command312 = Type("Command312")
        Command313 = Type("Command313")
        Command314 = Type("Command314")
        Command315 = Type("Command315")
        Command316 = Type("Command316")
        Command317 = Type("Command317")
        Command318 = Type("Command318")
        Command319 = Type("Command319")
        Command320 = Type("Command320")
        Command321 = Type("Command321")
        Command322 = Type("Command322")
        Command331 = Type("Command331")
        Command332 = Type("Command332")
        Command333 = Type("Command333")
        Command334 = Type("Command334")
        Command335 = Type("Command335")
        Command336 = Type("Command336")
        Command337 = Type("Command337")
        Command338 = Type("Command338")
        Command339 = Type("Command339")
        Command340 = Type("Command340")
        Command351 = Type("Command351")
        Command352 = Type("Command352")
        Command353 = Type("Command353")
        Command354 = Type("Command354")
        Command355 = Type("Command355")
        Command412 = Type("Command412")
        Command605 = Type("Command605")
        Command404 = Type("Command404")

        self.add_types(
            Command000, Command101, Command102, Command402, Command403, Command103, Command104, Command105,
            Command106, Command108, Command408, Command111, Command411, Command112, Command413,
            Command113, Command115, Command116, Command117, Command118, Command119, Command121,
            Command122, Command123, Command124, Command125, Command126, Command127, Command128,
            Command129, Command131, Command132, Command133, Command134, Command135, Command136,
            Command201, Command202, Command203, Command204, Command205, Command206, Command207,
            Command208, Command209, Command210, Command221, Command222, Command223, Command224,
            Command225, Command231, Command232, Command233, Command234, Command235, Command236,
            Command241, Command242, Command245, Command246, Command247, Command248, Command249,
            Command250, Command251, Command301, Command601, Command602, Command603, Command302,
            Command303, Command311, Command312, Command313, Command314, Command315, Command316,
            Command317, Command318, Command319, Command320, Command321, Command322, Command331,
            Command332, Command333, Command334, Command335, Command336, Command337, Command338,
            Command339, Command340, Command351, Command352, Command353, Command354, Command355,
            Command401, Command412, Command605, Command404
        )


class Package(Package):
    '''Core event Package, Contains event command processing'''
    def __init__(self):
        Package.__init__(self, "CORE_EVENTS_FORMAT", "CORE_EVENTS_FORMAT")
        self.setup_types()
        self.setup_events()
        self.setup_components()

    def setup_types(self):
        EventCommandFormater = Type("EventCommandFormater")
        self.add_types(EventFormaterType(), EventCommandFormater)

    def setup_events(self):
        pass

    def setup_components(self):
        commands = [
            ["Command000", Command000],
            ["Command101", Command101],
            ["Command401", Command401],
            ["Command102", Command102],
            ["Command402", Command402],
            ["Command403", Command403],
            ["Command103", Command103],
            ["Command104", Command104],
            ["Command105", Command105],
            ["Command106", Command106],
            ["Command108", Command108],
            ["Command408", Command408],
            ["Command111", Command111],
            ["Command411", Command411],
            ["Command112", Command112],
            ["Command413", Command413],
            ["Command113", Command113],
            ["Command115", Command115],
            ["Command116", Command116],
            ["Command117", Command117],
            ["Command118", Command118],
            ["Command119", Command119],
            ["Command121", Command121],
            ["Command122", Command122],
            ["Command123", Command123],
            ["Command124", Command124],
            ["Command125", Command125],
            ["Command126", Command126],
            ["Command127", Command127],
            ["Command128", Command128],
            ["Command129", Command129],
            ["Command131", Command131],
            ["Command132", Command132],
            ["Command133", Command133],
            ["Command134", Command134],
            ["Command135", Command135],
            ["Command136", Command136],
            ["Command201", Command201],
            ["Command202", Command202],
            ["Command203", Command203],
            ["Command204", Command204],
            ["Command205", Command205],
            ["Command206", Command206],
            ["Command207", Command207],
            ["Command208", Command208],
            ["Command209", Command209],
            ["Command210", Command210],
            ["Command221", Command221],
            ["Command222", Command222],
            ["Command223", Command223],
            ["Command224", Command224],
            ["Command225", Command225],
            ["Command231", Command231],
            ["Command232", Command232],
            ["Command233", Command233],
            ["Command234", Command234],
            ["Command235", Command235],
            ["Command236", Command236],
            ["Command241", Command241],
            ["Command242", Command242],
            ["Command245", Command245],
            ["Command246", Command246],
            ["Command247", Command247],
            ["Command248", Command248],
            ["Command249", Command249],
            ["Command250", Command250],
            ["Command251", Command251],
            ["Command301", Command301],
            ["Command601", Command601],
            ["Command602", Command602],
            ["Command603", Command603],
            ["Command302", Command302],
            ["Command303", Command303],
            ["Command311", Command311],
            ["Command312", Command312],
            ["Command313", Command313],
            ["Command314", Command314],
            ["Command315", Command315],
            ["Command316", Command316],
            ["Command317", Command317],
            ["Command318", Command318],
            ["Command319", Command319],
            ["Command320", Command320],
            ["Command321", Command321],
            ["Command322", Command322],
            ["Command331", Command331],
            ["Command332", Command332],
            ["Command333", Command333],
            ["Command334", Command334],
            ["Command335", Command335],
            ["Command336", Command336],
            ["Command337", Command337],
            ["Command338", Command338],
            ["Command339", Command339],
            ["Command340", Command340],
            ["Command351", Command351],
            ["Command352", Command352],
            ["Command353", Command353],
            ["Command354", Command354],
            ["Command355", Command355],
            ["Command412", Command412],
            ["Command605", Command605],
            ["Command404", Command404]
        ]
        for command in commands:
            component = Component(command[1], command[0], "EventFormaterType", "" + command[0], "CORE_EVENTS_FORMAT", 1.0, self)
            self.add_component(component)

        self.add_component(Component(EventCommandFormater, "EventCommandFormater", None, "CommandFormater", "CORE_EVENTS_FORMAT", 1.0, self))

package = Package()
key = package.add_to_kernel()

# this line is only here because it is the core and should be enabled by default,
# if it was a normal plug-in it would be enabled else where
Manager.enable_packages(key)
