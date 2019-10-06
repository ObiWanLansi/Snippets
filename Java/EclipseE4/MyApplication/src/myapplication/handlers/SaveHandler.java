package myapplication.handlers;


import org.eclipse.e4.core.di.annotations.CanExecute;
import org.eclipse.e4.core.di.annotations.Execute;
import org.eclipse.e4.ui.workbench.modeling.EPartService;



/**
 *
 */
public class SaveHandler {

    /**
     * @param partService
     * @return
     */
    @CanExecute
    public boolean canExecute( EPartService partService ) {

        if (partService != null) {
            return !partService.getDirtyParts().isEmpty();
        }
        return false;
    }


    /**
     * @param partService
     */
    @Execute
    public void execute( EPartService partService ) {

        partService.saveAll(false);
    }
}
