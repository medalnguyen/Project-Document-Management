import wx


class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="TreeCtrl Example", size=(400, 600))

        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        # Tạo TreeCtrl
        self.tree = wx.TreeCtrl(
            panel,
            style=wx.TR_HAS_BUTTONS | wx.TR_HIDE_ROOT | wx.HSCROLL | wx.VSCROLL
        )

        # Root ẩn
        root = self.tree.AddRoot("Root")

        # ====================== Setup ======================
        setup = self.tree.AppendItem(root, "Setup")
        self.tree.AppendItem(setup, "Country")
        self.tree.AppendItem(setup, "Project")
        self.tree.AppendItem(setup, "Subprojects")
        self.tree.AppendItem(setup, "Level 1 Sequence")
        self.tree.AppendItem(setup, "Task Location")
        self.tree.AppendItem(setup, "PL Actors")

        # ---- Types ----
        types = self.tree.AppendItem(setup, "Types")
        self.tree.AppendItem(types, "Subsystem Types")
        self.tree.AppendItem(types, "Basic Function Types")
        self.tree.AppendItem(types, "Item Types")
        self.tree.AppendItem(types, "Disciplines")
        self.tree.AppendItem(types, "TASK ACTIVITIES")
        self.tree.AppendItem(types, "CCK TASK TYPES")
        self.tree.AppendItem(types, "STS TASK TYPES")
        self.tree.AppendItem(types, "PIP TASK TYPES")
        self.tree.AppendItem(types, "PRC TASK TYPES")
        self.tree.AppendItem(types, "FTS TASK TYPES")
        self.tree.AppendItem(types, "OTS TASK TYPES")
        self.tree.AppendItem(types, "PVP TASK TYPES")
        self.tree.AppendItem(types, "PRE TASK TYPES")
        self.tree.AppendItem(types, "FORM TYPES")
        self.tree.AppendItem(types, "PunchList Categories")
        self.tree.AppendItem(types, "PunchList Activities")
        self.tree.AppendItem(types, "PunchList Action By")

        # ---- Assoc Types Tasks ----
        assoc = self.tree.AppendItem(setup, "Assoc Types Tasks")
        self.tree.AppendItem(assoc, "Items - Tasks")
        self.tree.AppendItem(assoc, "Test Packs - Tasks")
        self.tree.AppendItem(assoc, "Basic Functions - Tasks")

        # Add vào layout
        sizer.Add(self.tree, 1, wx.EXPAND | wx.ALL, 5)
        panel.SetSizer(sizer)


if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    frame.Show()
    app.MainLoop()
