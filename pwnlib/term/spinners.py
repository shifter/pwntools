# -*- coding: utf-8 -*-
__all__ = ['spinners']

def billboard(msg, window):
    return [msg[i : i + window].ljust(window, ' ') for i in xrange(len(msg))]

spinners = [
    ['/.......','./......','../.....','.../....','..../...','...../..','....../.',
     '.......\\','......\\.','.....\\..','....\\...','...\\....','..\\.....','.\\......'],
    ['|', '/', '-', '\\'],
    ['q', 'p', 'b', 'd'],
    ['.', 'o', 'O', '0', '*', ' ', ' ', ' '],
    ['▁', '▃', '▄', '▅', '▆', '▇', '█', '▇', '▆', '▅', '▄', '▃'],
    ['┤', '┘', '┴', '└', '├', '┌', '┬', '┐'],
    ['←', '↖', '↑', '↗', '→', '↘', '↓', '↙'],
    ['◢', '◢', '◣', '◣', '◤', '◤', '◥', '◥'],
    ['◐', '◓', '◑', '◒'],
    ['▖', '▘', '▝', '▗'],
    ['.', 'o', 'O', '°', ' ', ' ', '°', 'O', 'o', '.', ' ', ' '],
    ['<', '<', '∧', '∧', '>', '>', 'v', 'v'],
    ]
