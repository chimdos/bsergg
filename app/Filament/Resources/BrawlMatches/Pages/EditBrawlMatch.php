<?php

namespace App\Filament\Resources\BrawlMatches\Pages;

use App\Filament\Resources\BrawlMatches\BrawlMatchResource;
use Filament\Actions\DeleteAction;
use Filament\Resources\Pages\EditRecord;

class EditBrawlMatch extends EditRecord
{
    protected static string $resource = BrawlMatchResource::class;

    protected function getHeaderActions(): array
    {
        return [
            DeleteAction::make(),
        ];
    }
}
