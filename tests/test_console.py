#!/usr/bin/python3
"""Test suite for the console"""


import sys
import models
import unittest
from io import StringIO
from console import HBNBCommand
from unittest.mock import create_autospec


class test_console(unittest.TestCase):
    """Test the console module"""
    def setUp(self):
        """setup for"""
        self.backup = sys.stdout
        self.capt_out = StringIO()
        sys.stdout = self.capt_out

    def tearDown(self):
        """."""
        sys.stdout = self.backup

    def create(self):
        """Create an instance of the HBNBCommand"""
        return HBNBCommand()

    def test_quit(self):
        """Test quit exists"""
        console = self.create()
        self.assertTrue(console.onecmd("quit"))

    def test_EOF(self):
        """Test EOF exists"""
        console = self.create()
        self.assertTrue(console.onecmd("EOF"))

    def test_ALL(self):
        """Test all exists"""
        console = self.create()
        console.onecmd("all")
        self.assertTrue(isinstance(self.capt_out.getvalue(), str))

    def test_show(self):
        """Test show exists"""
        console = self.create()
        console.onecmd("create User")
        id_user = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd("show User " + id_user)
        value = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertTrue(str is type(value))

    def test_show_class_name(self):
        """Test name missing message error"""
        console = self.create()
        console.onecmd("create User")
        id_user = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd("show")
        value = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertEqual("** class name missing **\n", value)

    def test_show_class_id(self):
        """Test id missing message error"""
        console = self.create()
        console.onecmd("create User")
        id_user = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd("show User")
        value = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertEqual("** instance id missing **\n", value)

    def test_show_no_instance_found(self):
        """Test no instance found message error"""
        console = self.create()
        console.onecmd("create User")
        id_user = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd("show User " + "123456789")
        value = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertEqual("** no instance found **\n", value)

    def test_create(self):
        """Test create if it works"""
        console = self.create()
        console.onecmd("create User")
        self.assertTrue(isinstance(self.capt_out.getvalue(), str))

    def test_class_name(self):
        """Test class name missing message error"""
        console = self.create()
        console.onecmd("create")
        value = (self.capt_out.getvalue())
        self.assertEqual("** class name missing **\n", value)

    def test_class_name_doesnt_exist(self):
        """Test class name doesn't exist message error"""
        console = self.create()
        console.onecmd("create Binita")
        value = (self.capt_out.getvalue())
        self.assertEqual("** class doesn't exist **\n", value)
