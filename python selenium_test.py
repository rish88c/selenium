import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # type: ignore


class TestTodoApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up Selenium WebDriver
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        cls.driver = webdriver.Chrome(options=options)
        # Implicit wait to handle dynamic elements
        cls.driver.implicitly_wait(10)
        cls.base_url = "http://localhost:8000"

    def test_add_todo_item(self):
        self.driver.get(self.base_url + "/todo")

        # Add a new todo item
        new_todo_text = "Test Todo Item"
        input_element = self.driver.find_element_by_name("newtodo")
        input_element.send_keys(new_todo_text)
        input_element.send_keys(Keys.RETURN)

        # Check if the todo item is added
        todo_items = self.driver.find_elements_by_class_name("todo-item")
        self.assertTrue(any(new_todo_text in item.text for item in todo_items))

    def test_delete_todo_item(self):
        self.driver.get(self.base_url + "/todo")

        # Add a new todo item to delete later
        new_todo_text = "Todo Item to Delete"
        input_element = self.driver.find_element_by_name("newtodo")
        input_element.send_keys(new_todo_text)
        input_element.send_keys(Keys.RETURN)

        # Delete the added todo item
        todo_items = self.driver.find_elements_by_class_name("todo-item")
        delete_button = todo_items[-1].find_element_by_class_name("delete-btn")
        delete_button.click()

        # Check if the todo item is deleted
        todo_items_after_delete = self.driver.find_elements_by_class_name(
            "todo-item")
        self.assertFalse(
            any(new_todo_text in item.text for item in todo_items_after_delete))

    def test_edit_todo_item(self):
        self.driver.get(self.base_url + "/todo")

        # Add a new todo item to edit later
        new_todo_text = "Todo Item to Edit"
        input_element = self.driver.find_element_by_name("newtodo")
        input_element.send_keys(new_todo_text)
        input_element.send_keys(Keys.RETURN)

        # Find the added todo item and click on edit
        todo_items = self.driver.find_elements_by_class_name("todo-item")
        edit_button = todo_items[-1].find_element_by_class_name("edit-btn")
        edit_button.click()

        # Edit the todo item
        edit_input_element = self.driver.find_element_by_name("editTodo")
        edited_text = "Edited Todo Item"
        edit_input_element.clear()
        edit_input_element.send_keys(edited_text)
        edit_input_element.send_keys(Keys.RETURN)

        # Check if the todo item is edited
        todo_items_after_edit = self.driver.find_elements_by_class_name(
            "todo-item")
        self.assertTrue(
            any(edited_text in item.text for item in todo_items_after_edit))

    @classmethod
    def tearDownClass(cls):
        # Close the WebDriver instance
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
